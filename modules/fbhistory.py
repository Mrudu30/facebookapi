import requests
import pymysql as p
import os

class Fbhistory:
    def connect(self):
        return p.connect(host="localhost",user="root",password="",database="facebookapp",charset = "utf8mb4")

    def get_all_fbpages(self):
        con = Fbhistory.connect(self)
        cursor = con.cursor()
        try:
            cursor.execute('SELECT * FROM fbpages')
            return cursor.fetchall()
        except:
            con.rollback()
            return False
        finally:
            con.close()

    def caption_with_image(self, image_path, page_info):
        page_id = page_info[1]
        page_access_token = page_info[3]
        url = f"https://graph.facebook.com/{page_id}/photos"
        with open(image_path, 'rb') as image_file:
            files = {'source': image_file}
            params = {"access_token": page_access_token,"published":False}
            response = requests.post(url, params=params, files=files)
            post_data = response.json()
            if "error" in post_data:
                print("Error uploading photo:", post_data["error"]["message"])
                return False
            return post_data['id']

    def fbposts(self, data, image_path):
        con = self.connect()
        cursor = con.cursor()

        try:
            print('data:', data)
            cursor.execute('SELECT * FROM fbpages WHERE page_name=%s', (data['page_name'],))
            page_info = cursor.fetchone()
            print("page info: ", page_info)
            page_id = page_info[1]

            if image_path:
                photo_id = self.caption_with_image(image_path, page_info)
                attached_media = [{"media_fbid": str(photo_id)}]
                page_access_token = page_info[3]
                params = {
                    "access_token": page_access_token,
                    "attached_media":f"{attached_media}",
                    "message": data['message']
                }
                print(params)
                post_response = requests.post(f"https://graph.facebook.com/{page_id}/feed", data=params)
                post_result = post_response.json()
                if "error" in post_result:
                    print("2nd error")
                    print("Error creating post:", post_result["error"]["message"])
                    return None
                else:
                    post_id = post_result['id']
            else:
                page_id = page_info[1]
                page_access_token = page_info[3]
                url = f"https://graph.facebook.com/{page_id}/feed"
                params = {
                    "access_token": page_access_token,
                    "message": data['message']
                }
                response = requests.post(url, params=params)
                post_data = response.json()
                if "error" in post_data:
                    print("Error creating post:", post_data["error"]["message"])
                    return False
                post_id = post_data['id']

            print(post_id)
            cursor.execute('INSERT INTO posthistory(post_id,message,page_id) VALUES (%s,%s,%s)',(post_id, data['message'], page_id))
            con.commit()
            return True
        except Exception as e:
            print(e)
            con.rollback()
            return False
        finally:
            con.close()

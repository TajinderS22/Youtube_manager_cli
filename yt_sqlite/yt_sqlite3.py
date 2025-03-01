import sqlite3

conn = sqlite3.Connection("youtube_videos.db")

cursor = conn.cursor()

cursor.execute('''
    CREATE TABLE IF NOT EXISTS videos(
               id INTEGER PRIMARY KEY,
               name TEXT NOT NULL,
               time TEXT NOT NULL
    )

''')


def list_videos():
    print("\n")
    print("*"*60)
    cursor.execute(" SELECT * FROM videos")
    for row in cursor.fetchall():
       print(row)

    print("\n")
    print("*"*60)
    
def add_video(name,time):
    cursor.execute("INSERT INTO videos (name,time) VALUES (?,?)",(name,time))
    conn.commit()
def update_video(id, new_name,new_time):
    cursor.execute(" UPDATE videos SET name=? ,time=? WHERE id=?",(new_name,new_time,id))
    

def delete_video(id):
    cursor.execute( "DELETE FROM videos WHERE id=?",(id,))
    conn.commit()

def main():
    while True:

        print("\n Youtube videos manager ")
        print("1. list videos : ")
        print("2. Add Videos :")
        print("3. Update Video details : ")
        print("4. Delete a Video")
        print("5. Exit the app")

        choice= input("please select an option from above ")

        match choice:
            case '1':
                list_videos()
            case '2':
                name=input("Enter the name of video : ")
                time= input(" Enter the duration of video: ")
                add_video(name,time)
            case '3':
                list_videos()
                video_id=input("Please Enter the video Id: ")
                name=input("Please Enter the new name of video: ")
                time= input("please Enter the updated duration of video :")
                update_video(video_id,name,time)
            case '4':
                list_videos()
                video_id=input("please enter the Id of the video you want to delete :")
                delete_video(video_id)
            case '5':
                break
            case _:
                print("Please choose the valid Option ")

    conn.close()

if __name__=="__main__":
    main()


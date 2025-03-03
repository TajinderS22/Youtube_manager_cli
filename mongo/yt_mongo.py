from pymongo import MongoClient # type: ignore
from bson import ObjectId

client = MongoClient('mongodb+srv://tajinderyoutubepy:tajinderyoutubepy@cluster0.4uif2.mongodb.net/')
# It is not good thing to leave password as it is 

db=client["ytmanager"]
video_collection= db["videos"]
print(video_collection)


def list_videos():
    print("\n")
    print("*"*60)
    for video in video_collection.find():
        print(f"{video["_id"]}. {video["name"]}  Duration {video['time']}\n ")
    print("\n")
    print("*"*60)

def add_video(name, time):
    video_collection.insert_one({'name':name,'time':time})

def update_video(id, name, time):
    video_collection.update_one(
        {
        '_id':ObjectId(id),
        },
        {'$set':{'name': name,
        'time':time
        }}
    )
def delete_video(id):
    video_collection.delete_one({'_id':ObjectId(id) })


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



if __name__=="__main__":
    main()
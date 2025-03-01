
import json

youtube_text_file='youtube.txt'

def load_data():
    # try catch for handling errors 
    try:
        # open file in read mode as file
        with open(youtube_text_file, 'r')as file:
            return json.load(file)
    except FileNotFoundError:
        return []
    finally:
        pass

def save_data_helper( videos):
    with open(youtube_text_file,'w') as file:
        json.dump(videos,file)


def list_all_videos(videos):
    if videos==[]:
        print("File is empty please add your favourite videos")
        return
    print('\n')
    print("*"*70)
    for index,video in enumerate(videos,start =1):
        # we get index with the help of enumerate and hence make it possible to track easily 
        # video is an object with dict data type so we need to use key value noation to represent elements 
        print(f"{index}.{video['name']} duration: {video['time']}")
    print('\n')
    print("*"*70)


def add_videos(videos):
    video_name=input("Enter Video Name :")
    video_time=input("Enter Video Time :")
    videos.append({"name":video_name, "time":video_time})  
    save_data_helper(videos)  


def update_videos(videos):
    list_all_videos(videos)

    index = int(input("Enter the index of the video you want to update: "))
    if 1<=index<=len(videos):
        new_video_name=input("Enter the new video's name: ")
        new_video_duration= input(" Enter the duration of new video: ")
        if new_video_name and new_video_duration:
            videos[index-1]={'name':new_video_name, 'time':new_video_duration}
        elif new_video_duration:
            videos[index-1]={'name':videos[index-1]['name'],'time':new_video_duration}
        elif new_video_name:
            videos[index-1]={'name':new_video_name, 'time':videos[index-1]["time"]}

        save_data_helper(videos)
    else:
        print("Please select the valid index :)")


def delete_videos(videos):
    list_all_videos(videos)
    index=int(input("Enter the no of video you want to delete : "))

    if 1<= index <=len(videos):
        del videos[index-1]
        save_data_helper(videos)
    else:
        print("Invalid index selected  ")

def main():
    videos=load_data()

    while True:
        print("----> Youtube Manager <----")
        print("1. List your favourite videos. : ")
        print("2. Add your favourite video. : ")
        print("3. Update a Youtube video details. : ")
        print("4. Delete a Youtube Video. : ")
        print("5. Exit the app. : ")

        choice= input("Enter your choice : ")

        # print(videos)

        # Learn about match keyword and its usage---->

        match choice: 

            case '1':
                list_all_videos(videos)
            case '2':
                add_videos(videos)
            case '3': 
                update_videos(videos)
            case '4':
                delete_videos(videos)
            case '5':
                break
            case _:
                print("Invalid Choice")

            
        
    
# --->Industry standard--->
# if file contain any function named main then execute it 
if __name__=="__main__":
    main()

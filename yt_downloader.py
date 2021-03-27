from pytube import YouTube
from moviepy.editor import VideoFileClip
import shutil
import os
import subprocess
import datetime

# Main loop:
loop = True
while loop:
    link = input('Enter YouTube link: ')
    # YouTube object - contains API for a given link, e.g. yt.title.
    yt = YouTube(link)
    qlist = []
    printed_qlist = []

    # Title.
    print('')
    print('Title:', yt.title)
    # Length.
    t = str(datetime.timedelta(seconds = yt.length))
    print('Length:', t, '\n')

    # Download/que loop.
    dl_q_loop = True
    while dl_q_loop:
        dl_q = input("'d' = download, 'q' = queue, 'e' = exit: ")
        if dl_q == 'd':
            dl_loop = True
            while dl_loop:
                va = input("'v' = video, 'a' = audio, 'e' = exit: ")
                print('')
                if va == 'v':
                    # Grab highest possible progressive stream (mp4 file - 720p max).
                    high_res_va = yt.streams.get_highest_resolution()

                    # Download mp4.
                    print('Downloading...')
                    mp4_path = high_res_va.download()
                    print('Download complete!.\n')

                    # # Open mp4 with Transcribe!
                    # tr_loop = True
                    # while tr_loop:
                    #     transcribe = input("Open file with Transcribe!? - 'y' or 'n': ")
                    #     if transcribe == 'y':
                    #         # Apps require executable path rather than directory path, like below.
                    #         path_to_Transcribe = '/Applications/Transcribe!.app/Contents/MacOS/Transcribe!'
                    #         # arg[0] = program to run, arg[1,etc.] = writes onto arg[0].
                    #         subprocess.call([path_to_Transcribe, mp4_path])
                    #         break
                    #     elif transcribe == 'n':
                    #         break

                    # Back to Main.
                    dl_loop = False
                    dl_q_loop = False

                elif va == 'a':
                    # Download mp4 first.
                    high_res_va = yt.streams.get_highest_resolution()
                    print('Downloading', yt.title + '.mp4...')
                    mp4_path = high_res_va.download()
                    print(yt.title + '.mp4 complete.\n')

                    # Convert mp4 to mp3.
                    print('Converting to mp3...')
                    mp3_filename = yt.title + '.mp3' # Append mp3 extension to title and save as filename. 
                    videoclip = VideoFileClip(mp4_path) # Grab mp4 file.
                    audioclip = videoclip.audio # Extract audio codec from mp4 file.
                    audioclip.write_audiofile(mp3_filename) # Write to audiofile with mp3 filename.
                    videoclip.close()
                    audioclip.close()

                    # # Change location to Desktop folder (moviepy writes to current directory).
                    # mp3_final = shutil.move('/Users/yoon/Dev/yt-downloader/' + mp3_filename,
                    #     '/Users/yoon/Desktop/' + mp3_filename)
                    # print('Audio saved to Desktop folder.\n')

                    # Delete mp4 file.
                    os.remove(mp4_path)

                    # # Open mp3 with Transcribe!.
                    # tr_loop = True
                    # while tr_loop:
                    #     transcribe = input("Open file with Transcribe!? - 'y' or 'n': ")
                    #     if transcribe == 'y':
                    #         path_to_Transcribe = '/Applications/Transcribe!.app/Contents/MacOS/Transcribe!'
                    #         subprocess.call([path_to_Transcribe, mp3_final])
                    #         break
                    #     elif transcribe == 'n':
                    #         break

                    # Back to Main.
                    dl_loop = False
                    dl_q_loop = False

                elif va == 'e':
                    # Back to Main.
                    dl_loop = False
                    dl_q_loop = False

        elif dl_q == 'q':
            q_loop = True
            while q_loop:
                # Add video object to queue list.
                qlist.append(yt)
                # Queue list with titles printed.
                printed_qlist.append(yt.title)
                print('Queue:', printed_qlist, '\n')

                addq_loop = True
                while addq_loop:
                    addq = input("Add another video? 'y' or 'n': ")
                    if addq == 'y':
                        link = input('Enter YouTube link: ')
                        yt = YouTube(link)

                        print('')
                        print('Title:', yt.title)
                        t = str(datetime.timedelta(seconds = yt.length))
                        print('Length:', t, '\n')
                        break 
                    
                    elif addq == 'n':
                        no_q_loop = True
                        while no_q_loop:
                            dl_qlist = input("'d' = download videos, 'c' = convert videos to mp3 and download, 'e' = exit: ")
                            if dl_qlist == 'd':
                                for v in qlist:
                                    # Grab highest possible progressive stream (mp4 file - 720p max).
                                    high_res_va = v.streams.get_highest_resolution()

                                    # Download mp4 to Desktop folder.
                                    print('')
                                    print('Downloading', v.title + '...')
                                    mp4 = high_res_va.download()
                                    print('Download complete!.\n')

                                    # Back to Main.
                                    no_q_loop = False
                                    addq_loop = False
                                    q_loop = False
                                    dl_q_loop = False

                            elif dl_qlist == 'c':
                                for v in qlist:
                                    # Download mp4 first.
                                    high_res_va = v.streams.get_highest_resolution()
                                    print('')
                                    print('Downloading', v.title + '.mp4...')
                                    mp4_path = high_res_va.download()
                                    print(v.title + '.mp4 complete.\n')

                                    # Convert mp4 to mp3.
                                    print('Converting to mp3...')
                                    mp3_filename = v.title + '.mp3'
                                    videoclip = VideoFileClip(mp4_path)
                                    audioclip = videoclip.audio
                                    audioclip.write_audiofile(mp3_filename)
                                    videoclip.close()
                                    audioclip.close()

                                    # # Change location to Desktop folder.
                                    # mp3_final = shutil.move('/Users/yoon/Dev/yt-downloader/' + mp3_filename,
                                    #     '/Users/yoon/Desktop/' + mp3_filename)
                                    # print('Audio saved to Temp Items folder.\n')

                                    # Delete mp4 file.
                                    os.remove(mp4_path)

                                    # Back to Main.
                                    no_q_loop = False
                                    addq_loop = False
                                    q_loop = False
                                    dl_q_loop = False

                            elif dl_qlist == 'e':
                                # Back to Main.
                                no_q_loop = False
                                addq_loop = False
                                q_loop = False
                                dl_q_loop = False

        elif dl_q == 'e':
            break




from pytube import YouTube
from moviepy.editor import *
import shutil
import os
import subprocess
import datetime

# Main loop:
loop = True
while loop:
    link = input('Enter YouTube link: ') # try and except for invalid links
    yt = YouTube(link)
    qlist = []
    printed_qlist = []

    # Title:
    print('')
    print('Title:', yt.title)
    # Length:
    t = str(datetime.timedelta(seconds = yt.length))
    print('Length:', t, '\n') # change to minutes

    # Download/que loop:
    dl_q_loop = True
    while dl_q_loop:
        dl_q = input("'d' = download, 'q' = queue, 'e' = exit: ")
        if dl_q == 'd':
            dl_loop = True
            while dl_loop:
                va = input("'v' = video + audio, 'a' = audio, 'e' = exit: ")
                print('')
                if va == 'v':
                    # Grab highest res progressive stream (mp4 file - 720p max):
                    high_res_va = yt.streams.get_highest_resolution()

                    # Download mp4 to Temp Items folder:
                    print('Downloading...')
                    mp4 = high_res_va.download('C:/Users/rhffc/OneDrive/Desktop/Temp Items')
                    print('Download complete! Saved to Temp Items folder.\n')

                    # Open mp4 with Transcribe!
                    tr_loop = True
                    while tr_loop:
                        transcribe = input("Open file with Transcribe!? - 'y' or 'n': ")
                        if transcribe == 'y':
                            path_to_Transcribe = 'C:/Program Files (x86)/Transcribe!/Transcribe.exe'
                            subprocess.call([path_to_Transcribe, mp4])
                            break
                        elif transcribe == 'n':
                            break

                    # Back to Main:
                    dl_loop = False
                    dl_q_loop = False
                elif va == 'a':
                    # Download mp4 first:
                    high_res_va = yt.streams.get_highest_resolution()
                    print('Downloading', yt.title + '.mp4...')
                    mp4 = high_res_va.download('C:/Users/rhffc/OneDrive/Desktop/Temp Items')
                    print(yt.title + '.mp4 complete.\n')

                    # Convert mp4 to mp3:
                    print('Converting to mp3...')
                    mp3_file = yt.title + '.mp3' # .mp3 file
                    videoclip = VideoFileClip(mp4) # Grab mp4 file
                    audioclip = videoclip.audio # Extract mp3 from grabbed mp4 file
                    audioclip.write_audiofile(mp3_file) # Convert extracted mp3 file to .mp3 file
                    videoclip.close()
                    audioclip.close()

                    # Change location to Temp Items folder:
                    mp3_final = shutil.move('C:/Users/rhffc/OneDrive/Desktop/Programming/Projects/yt_downloader/' + mp3_file,
                        'C:/Users/rhffc/OneDrive/Desktop/Temp Items/' + mp3_file)
                    print('Audio saved to Temp Items folder.\n')

                    # Delete mp4 file:
                    os.remove(mp4)

                    # Open mp4 with Transcribe!:
                    tr_loop = True
                    while tr_loop:
                        transcribe = input("Open file with Transcribe!? - 'y' or 'n': ")
                        if transcribe == 'y':
                            path_to_Transcribe = 'C:/Program Files (x86)/Transcribe!/Transcribe.exe'
                            subprocess.call([path_to_Transcribe, mp3_final])
                            break
                        elif transcribe == 'n':
                            break

                    # Back to Main:
                    dl_loop = False
                    dl_q_loop = False
                elif va == 'e':
                    # Back to Main:
                    dl_loop = False
                    dl_q_loop = False
        elif dl_q == 'q':
            q_loop = True
            while q_loop:
                # Add video object to queue list:
                qlist.append(yt)
                # Queue list with titles, printed:
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
                        break # break out of addq_loop, return to q_loop
                    elif addq == 'n':
                        no_q_loop = True
                        while no_q_loop:
                            dl_qlist = input("'d' = download queue, 'c' = convert videos to mp3 and download, 'e' = exit: ")
                            if dl_qlist == 'd':
                                for v in qlist:
                                    high_res_va = v.streams.get_highest_resolution()

                                    print('')
                                    print('Downloading', v.title + '...')
                                    mp4 = high_res_va.download('C:/Users/rhffc/OneDrive/Desktop/Temp Items')
                                    print('Download complete! Saved to Temp Items folder.\n')

                                    # Back to Main:
                                    no_q_loop = False
                                    addq_loop = False
                                    q_loop = False
                                    dl_q_loop = False
                            elif dl_qlist == 'c':
                                for v in qlist:
                                    # Download mp4 first:
                                    high_res_va = v.streams.get_highest_resolution()
                                    print('')
                                    print('Downloading', v.title + '.mp4...')
                                    mp4 = high_res_va.download('C:/Users/rhffc/OneDrive/Desktop/Temp Items')
                                    print(v.title + '.mp4 complete.\n')

                                    # Convert mp4 to mp3:
                                    print('Converting to mp3...')
                                    mp3_file = v.title + '.mp3'
                                    videoclip = VideoFileClip(mp4)
                                    audioclip = videoclip.audio
                                    audioclip.write_audiofile(mp3_file)
                                    videoclip.close()
                                    audioclip.close()

                                    # Change location to Temp Items folder:
                                    mp3_final = shutil.move('C:/Users/rhffc/OneDrive/Desktop/Programming/Projects/yt_downloader/' + mp3_file,
                                        'C:/Users/rhffc/OneDrive/Desktop/Temp Items/' + mp3_file)
                                    print('Audio saved to Temp Items folder.\n')

                                    # Delete mp4 file:
                                    os.remove(mp4)

                                    # Back to Main:
                                    no_q_loop = False
                                    addq_loop = False
                                    q_loop = False
                                    dl_q_loop = False
                            elif dl_qlist == 'e':
                                # Back to Main:
                                no_q_loop = False
                                addq_loop = False
                                q_loop = False
                                dl_q_loop = False
        elif dl_q == 'e':
            break




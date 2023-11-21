import ffmpeg

class VideoProcessor:
    def cut_macroblocks_motionvectors(self, input_video, start_time, duration, output_video):
        (
            ffmpeg.input(input_video, ss=start_time, t=duration)
            .output(output_video, vf='codecview=mv=pf+bf')
            .run()
        )
    
    def create_container(self, input_file, output_file):
        ffmpeg.output(ffmpeg.input(input_file, t=50), 'S2_VIDEO_205574/container/temp_video.mp4').run()
        ffmpeg.output(ffmpeg.input('S2_VIDEO_205574/temp_video.mp4'), 'S2_VIDEO_205574/container/audio_mono.mp3', ac=1).run()
        ffmpeg.output(ffmpeg.input('S2_VIDEO_205574/container/temp_video.mp4'), 'S2_VIDEO_205574/container/audio_stereo.mp3', ab='128k').run()
        ffmpeg.output(ffmpeg.input('S2_VIDEO_205574/container/temp_video.mp4'), 'S2_VIDEO_205574/container/audio.aac', acodec='aac').run()

        ffmpeg.concat(
            ffmpeg.input('S2_VIDEO_205574/container/temp_video.mp4'),
            ffmpeg.input('S2_VIDEO_205574/container/audio_mono.mp3'),
            ffmpeg.input('S2_VIDEO_205574/container/audio_stereo.mp3'),
            ffmpeg.input('S2_VIDEO_205574/container/audio.aac'),
            v=1, a=3
        ).output(output_file).run()
    
    def tracks(self, input_file):
        return len(ffmpeg.probe(input_file)['streams'])
    
    def subtitles(self, input_file, subs):
         ffmpeg.input(input_file).output('S2_VIDEO_205574/output.mp4', vf=f"subtitles='{subs}'").run()

processor = VideoProcessor()
# processor.cut_macroblocks_motionvectors('S2_(MORE)Python & Video/BBB.mp4', 300, 9, 'S2_(MORE)Python & Video/macroblocks/BBB_cut_vectors.mp4')
# processor.create_container('S2_(MORE)Python & Video/BBB.mp4', 'S2_(MORE)Python & Video/container/BBB.mp4')
#print(processor.tracks('S2_(MORE)Python & Video/container/BBB.mp4'))
processor.subtitles('S2_VIDEO_205574/BBB.mp4', 'S2_VIDEO_205574/subtitles/subtitles.srt')
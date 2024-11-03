# TEAM MEETING

## Updates

### Speech-to-text (STT) model
- A vosk model; loads fast and only requires the models to be installed rather than having to be imported like Whisper.
- The Vosk model records partials at the dictated sample rate.
- With those, the model tries to average the samples otu to get the actual transcrption, and then prints it out.
- IL will work on updating this to enhance accuracy, as it is vulnerable to noise. 
- BM queried whether it is primarily platinum code. IL affirmed.
- BM queried whether it imports multiple Python modules. 
  - IL noted it imports the operating system Q, which is already built with platinum. It imports sound device, which is whatever the sound device (microphone) is, and it imports vosk, and JSON so it can read files.
- BM queried whether it is being run from a project directory called vosk. 
  - IL runs the model directly on his laptop, as the folder is already there.
    - The file - depending on what vosk model we require - can be downloaded and imported.
    - IL noted we may need to pip install the vosk as well.
    - Then we can give it the directory path to the model.
- BM indicated it could be useful for him to replicate IL's work on a different computer, to ensure it can be replicated.
  - IL agreed, but noted more time to refine the model before replication would be ideal.
- SPN queried whether there were unexpected encounters or troubleshooting required while training the model?
  - IL noted the model was pre-trained and only required slight modification to run. IL however noted the model is very sensitive and picks up everything.
  - For example, one transcription says "Public as the lightest model and as a varying high school derives its one lttle probably rather reply."
    - It does not make sense as multiple people were speaking.
- SPN queried whether the sensitivity may have anything to do with the microphone itself. 
  - IL indicated it is unlikely, but is still in the process of working it out.
- BM noted IL began with using Whisper, and queried whether it was too slow. 
  - IL found that it was not printing transcriptions in real-time. IL further noted he will experiment with Whisper again, but it does not look promising.
- AT asked how IL put this lip-reading model together.
  - IL noted there is a lip-reading model on Hugging Face, called SilentSpeak/LipCoordNet (https://huggingface.co/SilentSpeak/LipCoordNet )
  - SilentSpeak builds off of the LipCoordNet model (lipnet), a fairly well-developed lip-reading model that IL was researching on.
  - IL took the repository, downloaded the data which contains about 2.5 million data points and began training it.
  - It functions like a 3D convolution network with some partial adversary built into it.
- BM queried whether IL is trying to converge on a certain accuracy.
- BM queried the name of the dataset.
  - Grid Corpus is the main dataset, along with another dataset called EEGLLC, which is also from the Grid Corpus datset.
  - BM noted Grid Corpus sounds like it is a data set of whole bodies.
- AT queried how the model is run.
  - IL noted the model is run on his laptop for now, but can be put onto a microcontroller as long as the microcontroller has a camera.
  - IL further noted to make it live, there needs to be a recording and then have that recording be able to be split into a series of JPEGs, which is quite easy to do, and relatively depending on the quality of the video input, with varying accuracy.
- AT queried whether we need to document the alignment algorithms.
  - The string, alignment character is just a modified I want to say modified, it’s just a Needleman Wunsch algorithm which is used to align alleles in gene sequence. 
  - Tt usually only 4 letters, but you can make it arbitrary so it just matches any characters that you want it to match. 
  - It pits them against each other and then it’s like a score, so if it’s a match it’s a one, if it’s a mis-match it’s a negative one, if it's a gap it’s one. 
  - The idea is it tries to align them together. So it starts from the bottom and it tries to find the optimal path of alignment up, and then it prints out the max alignment. 
  - What it does is once it has both of the texts aligned, it will align them the best it can, and then it’ll put dashes in between things where it can’t align, and then, you put that into another function that basically combines the two aligns, and if there’s full agreement in a character, that character goes in that position otherwise it gets a space or dash depending. 
  - From there, IL just put in the match percentage to tell how strong the connection is between the two alignments. 
  - That is all printed on IL's computer, so that’s all done. IL is going to modify it so that if it has a certain match percentage threshold that it doesn’t combine and instead just takes one of the strings that it is most confident the most full of alignment information basically and then go from there. 

### Lip-reading model
- Raspberry Pi Camera Module 3 captures short video.
- The video is fed to the model, and is essentially converted into a series of JPEGs. 
- As at now, the model splits video input into 70 JPEGs (this number can be altered)
- The model then analyses the series sequentially, looking at the lip position and watches in each frame how it moves or how it varies in each frame. 
- From there, it will extract a word, or a letter, and it will repeat that process constantly. 
- It will then print out a string of letters of what it perceives as being said, or it may print out an error rate or a comment.
- There may be difficulties pinpointing the lips of the speaker in the video.
- The model is currently trained from 34 speakers from the UK. There will be a need to review the training dataset to account for any possible bias.
- There is an alternative, which involves taking a picture with the camera x amount of times, offset to a file, have the model translate it, have a second file with whatever is being done then, and then have an x amount of offsets that gets translated sequentially.
- This alternative requires the system to run multiple things at once, which may be resource intensive. 


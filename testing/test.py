
import torch


# x = torch.tensor([1.0])
#
# y = torch.tensor([2.0])
# w = torch.tensor([1.0], requires_grad=True)
#
# # Forward pass
# y_hat = w*x
# loss = (y_hat-y)**2
#
# print(loss)
#
#
# # Backward pass
# loss.backward()
# print(w.grad)
#
# ### update weights
# # next forward / backward pass

import speech_recognition as sr
print(sr.__version__) # just to print the version not required
r = sr.Recognizer()
my_mic = sr.Microphone(device_index=2) #my device index is 1, you have to put your device index
with my_mic as source:
    print("Say now!!!!")
    r.adjust_for_ambient_noise(source) #reduce noise
    audio = r.listen(source) #take voice input from the microphone
print(r.recognize_google(audio)) #to print voice into text



# gradient

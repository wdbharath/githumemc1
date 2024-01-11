
import streamlit as st
from rembg import remove
from PIL import Image


def removebg(img):
    input=Image.open(img)
    return remove(input)
    
    
    
    
def main():
    st.title("Background Remover App")
    upload=st.file_uploader("Choose an Image...",type=["jpeg","jpg","png"])
    
    if upload is not None:
        st.image(upload,caption="Uploaded Image")
        st.write("Processing......")
        result=removebg(upload)
        st.image(result,caption="Result")
    
if __name__=='__main__':
    main()
    

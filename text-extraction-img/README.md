# **Using OCR to Extract Text from Images**

-By Ananya Drishti

Used many OCRs to extract text from image.
One of them is pyTesseract. 
On Jupyter Notebook, installed tesseract OCR, libtesseract OCR, pytesseract. 
For results, in big font, it took “ “ to be alphanumeric values, subscripts were not read. 
It returns invoice tables as plain text. There are errors in the data extracted.

For TROCR I got ValueError: Invalid image type. Expected either PIL.Image.Image, numpy.ndarray, torch.Tensor, tf.Tensor or jax.ndarray, but got <class 'str'>.

In KerasOCR, I worked with Tensorflow OCR. There were some discrepancy issues, but it worked.
Used pipeline to read multiple images a once. I also generated text predictions from the images.
A cod snippet was written to plot the text predictions as comments on the images.
It also managed to print the predicted text on the output area. One con was that each word was printed on a ne line. 

Using EasyOCR, I imported Image from PIL. Used .reader and .readText to extract text and the probability of its accuracy.

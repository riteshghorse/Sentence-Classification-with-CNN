# Sentence-Classification-with-CNN
**[This code originally belongs to the "Implementing a CNN for Text Classification in Tensorflow" blog post.](http://www.wildml.com/2015/12/implementing-a-cnn-for-text-classification-in-tensorflow/)**

It is slightly simplified implementation of Kim's [Convolutional Neural Networks for Sentence Classification](http://arxiv.org/abs/1408.5882) paper in Tensorflow.

### Description
The CNN model is trained on tweets addressed to Railway Ministry. Labelling of data was done manually on [labelbox.](https://labelbox.com)

The model is trained to classify tweets into seven categories: "appreciation", "hygiene", "poor service", "request new service", "security problem", "staff complain" and "train delay".

The accuarcy achieved over unseen data is 71%.

## How to run 
Run server by following command:
```
python manage.py runserver
```

## Train your model
put your data inside data directory in personal/classification_model/

zip your data.csv file as data.csv.zip

cd to personal/classification_model/

And run following command to train the model:
```
python3 train.py ./data/data.csv.zip ./parameters.json
```

## Test the model
Don't forget to change the 'checkpoint dir' in predict.py if you retrain the model.
```
python3 predict.py ./data/small_samples.json
```

## Requirements

- Python 3
- Tensorflow > 0.12
- Django



## References

- [Convolutional Neural Networks for Sentence Classification](http://arxiv.org/abs/1408.5882)
- [A Sensitivity Analysis of (and Practitioners' Guide to) Convolutional Neural Networks for Sentence Classification](http://arxiv.org/abs/1510.03820)
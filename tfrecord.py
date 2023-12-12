from xml.etree import ElementTree as ET

import tensorflow as tf


def create_tf_example(xml_file, img_path):
    # Analizza il file XML
    tree = ET.parse(xml_file)
    root = tree.getroot()

    # Leggi le dimensioni dell'immagine
    width = int(root.find('size/width').text)
    height = int(root.find('size/height').text)

    # Leggi l'immagine
    with tf.io.gfile.GFile(img_path, 'rb') as fid:
        encoded_img = fid.read()

    # Crea un TFRecord
    tf_example = tf.train.Example(features=tf.train.Features(feature={
        'image/height': tf.train.Feature(int64_list=tf.train.Int64List(value=[height])),
        'image/width': tf.train.Feature(int64_list=tf.train.Int64List(value=[width])),
        'image/encoded': tf.train.Feature(bytes_list=tf.train.BytesList(value=[encoded_img])),
        'image/format': tf.train.Feature(bytes_list=tf.train.BytesList(value=[b'jpg'])),
        # Aggiungi qui altre feature necessarie
    }))

    return tf_example


def main():
    # Percorso del file XML e dell'immagine
    xml_file = 'G:/VideoPack2/_Awards31_secondo_00-00-05.xml'
    img_path = 'G:/VideoPack2/_Awards31_secondo_00-00-05.jpg'

    # Crea un writer TFRecord
    writer = tf.io.TFRecordWriter('output.tfrecord')

    # Crea un esempio TFRecord
    tf_example = create_tf_example(xml_file, img_path)

    # Scrivi l'esempio in un file TFRecord
    writer.write(tf_example.SerializeToString())
    writer.close()


if __name__ == '__main__':
    main()

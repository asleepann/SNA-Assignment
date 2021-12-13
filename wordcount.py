import sys
from pyspark import SparkConf, SparkContext


def main():

    if len(sys.argv) != 3:
        print('Usage job.py <input_dir> <output_dir>')
        sys.exit(1)

    in_dir = sys.argv[1]
    out_dir = sys.argv[2]

    conf = SparkConf().setAppName("Word count - PySpark")
    sc = SparkContext(conf=conf)

    text_file = sc.textFile(in_dir)
    counts = text_file.flatMap(lambda line: line.split(" ")) \
        .map(lambda word: (word, 1)) \
        .reduceByKey(lambda a, b: a + b)
        
    counts.saveAsTextFile(out_dir)


if __name__ == "__main__":
    main()

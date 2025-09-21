import argparse
from pyspark.sql import SparkSession
from pyspark.ml import PipelineModel
from pyspark.ml.evaluation import MulticlassClassificationEvaluator


def main():
    parser = argparse.ArgumentParser(description="Evaluate a pre-trained Spark ML Model")
    parser.add_argument("--model_path", required=True, type=str, help="Path to the trained model")
    parser.add_argument("--test_path", required=True, type=str, help="Path to the test data(Must be a Parquet file")
    args = parser.parse_args()

    label_col = "stock_out_signal"
    prediction_col = "prediction"

    spark = SparkSession .builder .appName("model_evaluate") .getOrCreate()

    #Load model and test data
    model = PipelineModel.load(args.model_path)

    # Load test data
    test_df = spark.read.parquet(args.test_path)

    # Generate predictions
    pred_df = model.transform(test_df)

    # Class distribution
    class_dist = pred_df.groupBy(label_col).count().orderBy(label_col).toPandas()

    # Metrics using Spark's MulticlassClassificationEvaluator
    evaluator_acc = MulticlassClassificationEvaluator(
        labelCol=label_col,predictionCol=prediction_col, metricName="accuracy"
    )
    evaluator_prec = MulticlassClassificationEvaluator(
        labelCol=label_col,predictionCol=prediction_col, metricName="weightedPrecision"
    )
    evaluator_recall = MulticlassClassificationEvaluator(
        labelCol=label_col,predictionCol=prediction_col, metricName="weightedRecall"
    )
    evaluator_f1 = MulticlassClassificationEvaluator(
        labelCol=label_col,predictionCol=prediction_col, metricName="f1"
    )

    accuracy = evaluator_acc.evaluate(pred_df)
    precision = evaluator_prec.evaluate(pred_df)
    recall = evaluator_recall.evaluate(pred_df)
    f1 = evaluator_f1.evaluate(pred_df)

    # Print summary
    print("\n===== Model Evaluation Summary =====")
    print(f"Accuracy : {accuracy:.4f}")
    print(f"Precision: {precision:.4f}")
    print(f"Recall   : {recall:.4f}")
    print(f"F1-Score : {f1:.4f}")
    print("Class Distribution:")
    for row in class_dist.to_dict(orient="records"):
        print(row)
    print("===================================\n")

    spark.stop()


if __name__ == "__main__":
    main()
import pytest
from chicagotaxi.etl_job import filter_duplicates


@pytest.mark.usefixtures("spark_session")
def test_filter_duplicates(spark_session):
    test_df = spark_session.createDataFrame(
        [
            ('hobbit', 'Samwise', 5),
            ('hobbit', 'Billbo', 50),
            ('hobbit', 'Billbo', 20),
            ('wizard', 'Gandalf', 1000)
        ],
        ['that_column', 'another_column', 'yet_another']
    )
    test_subset = ['another_column', 'yest_another']

    new_df = filter_duplicates(test_df, test_subset)
    assert new_df.columns.len() == len(test_df.columns) - len(test_subset)

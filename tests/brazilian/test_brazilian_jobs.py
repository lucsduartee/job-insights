from src.brazilian_jobs import read_brazilian_file


def test_brazilian_jobs():
    jobs = read_brazilian_file("tests/mocks/brazilians_jobs.csv")
    for job in jobs:
        assert "title" in job and "titulo" not in job
        assert "salary" in job and "salario" not in job
        assert "type" in job and "tipo" not in job

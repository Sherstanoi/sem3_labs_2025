import json
from sys import exit

from cm_timer import cm_timer_1
from gen_random import Gen_random
from print_result import print_result
from unique import Unique
# Сделаем другие необходимые импорты

@print_result
def f1(vacancies) -> list[str]:
    Jobs = [vacancy["job-name"] for vacancy in vacancies]
    return sorted(Unique(Jobs, case_sensitive=False))


@print_result
def f2(Jobs) -> list[str]:
    return list(filter(lambda Job: Job.startswith("программист"), Jobs[0]))


@print_result
def f3(Jobs) -> list[str]:
    return list(map(lambda Job: Job + " с опытом Python", Jobs))


@print_result
def f4(Jobs) -> list[str]:
    Salaries = Gen_random(len(Jobs), 100_000, 200_000)
    return [f"{Job}, зарплата {Salarys} руб." for Job, Salarys in zip(Jobs, Salaries)]



def main() -> int:
    with open("data_light.json", encoding="utf-8") as file:
        data = json.load(file)
    with cm_timer_1():
        f4(f3(f2(f1(data))))

    return 0


if __name__ == "__main__":
    exit(main())
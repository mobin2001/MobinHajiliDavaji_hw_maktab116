from math import floor


class InvalidName(BaseException):
    def __str__(self) -> str:
        return "invalid name"


class InvalidAgeInterval(BaseException):
    def __str__(self) -> str:
        return "invalid age interval"


class InvalidTimetype(BaseException):
    def __str__(self) -> str:
        return "invalid timetype"


class InvalidSalary(BaseException):
    def __str__(self) -> str:
        return "invalid salary"


class InvalidAge(BaseException):
    def __str__(self) -> str:
        return "invalid age"


class InvalidJobId(BaseException):
    def __str__(self) -> str:
        return "invalid index"


class InvalidSkillType(BaseException):
    def __str__(self) -> str:
        return "invalid skill"


class RepeatedSkill(BaseException):
    def __str__(self) -> str:
        return "repeated skill"


class Job:

    job_id = 1
    objects = {}

    def __init__(
        self, name: str, minage: str, maxage: str, time: str, salary: str
    ) -> None:
        Job.validate(name, minage, maxage, time, salary)
        self.name = name
        self.minage = int(minage)
        self.maxage = int(maxage)
        self.skills = []
        self.view = 0
        self.view_dict = {}
        self.timetype = time
        self.salary = int(salary)
        self.id = Job.job_id
        Job.job_id += 1
        Job.objects[self.id] = self

    @staticmethod
    def validate(name: str, minage: str, maxage: str, time: str, salary: str) -> BaseExceptionGroup:
        """staticmethod for validating job values"""
        minage = int(minage)
        maxage = int(maxage)
        salary = int(salary)

        if len(name) < 1 or len(name) > 10 or not name.isalpha():
            raise InvalidName

        if minage < 0 or maxage > 200:
            raise InvalidAgeInterval

        elif not minage <= maxage:
            raise InvalidAgeInterval

        if time not in ["FULLTIME", "PARTTIME", "PROJECT"]:
            raise InvalidTimetype

        if salary < 0 or salary > 999999999:
            raise InvalidSalary

        elif salary % 1000 != 0:
            raise InvalidSalary

    @classmethod
    def get(cls, id: int) -> object:
        """method for search and get job object by job id"""
        if id not in cls.objects:
            raise InvalidJobId
        return cls.objects[id]

    def __str__(self) -> str:

        finall_str = f"{self.name}-{self.view}-"

        if len(list(self.view_dict.items())) != 0:
            my_list = sorted(list(self.view_dict.items()), key=lambda x: (x[1], x[0]))
            for item in my_list:
                finall_str += f"({item[0]},{item[1]})"

        return finall_str


class User:

    user_id = 1
    objects = {}

    def __init__(self, name: str, age: str, time: str, salary: int) -> None:

        User.validate(name, age, time, salary)
        self.name = name
        self.age = int(age)
        self.timetype = time
        self.skills = []
        self.view_dict = {}
        self.score = []
        self.salary = int(salary)
        self.id = User.user_id
        User.user_id += 1
        User.objects[self.id] = self

    @staticmethod
    def validate(name: str, age: str, time: str, salary: str) -> None:
        """staticmethod for validating job values"""
        age = int(age)
        salary = int(salary)

        if len(name) < 1 or len(name) > 10 or not name.isalpha():
            raise InvalidName

        if age < 0 or age > 200:
            raise InvalidAge

        if time not in ["FULLTIME", "PARTTIME", "PROJECT"]:
            raise InvalidTimetype

        if salary < 0 or salary > 999999999:
            raise InvalidSalary
        elif salary % 1000 != 0:
            raise InvalidSalary

    @classmethod
    def get(cls, id: int) -> object:
        """method for search and get user object by user id"""
        if id not in cls.objects:
            raise InvalidJobId
        return cls.objects[id]

    def __str__(self) -> str:

        finall_str = f"{self.name}-"
        if len(list(self.view_dict.items())) != 0:
            my_list = sorted(list(self.view_dict.items()), key=lambda x: (x[1], x[0]))
            for item in my_list:
                finall_str += f"({item[0]},{item[1]})"

        return finall_str


def add_job_skill(job_id: str, skill: str) -> None:
    """function for add new skill for job"""
    job_id = int(job_id)
    job = Job.get(job_id)

    if skill not in skills:
        raise InvalidSkillType

    if skill in job.skills:
        raise RepeatedSkill

    job.skills.append(skill)
    job.view_dict[skill] = 0


def add_user_skill(user_id: int, skill: str) -> None:
    """function for add new skill for user"""
    user_id: int = int(user_id)
    user: object = User.get(user_id)

    if skill not in skills:
        raise InvalidSkillType

    if skill in user.skills:
        raise RepeatedSkill

    user.skills.append(skill)
    user.view_dict[skill] = 0


def view(user_id: str, job_id: str) -> None:
    user_id = int(user_id)
    job_id = int(job_id)
    user: object= User.get(user_id)
    job : object= Job.get(job_id)
    job.view += 1

    for item in job.skills:
        if item in user.skills:
            user.view_dict[item] += 1
            job.view_dict[item] += 1


def get_job(user_id: int) -> str:
    """function for calculating job scores for user with given id"""
    user_id = int(user_id)
    user: object = User.get(user_id)
    for job in Job.objects:
        score = 0
        job_obj: object = Job.get(job)
        time_job = job_obj.timetype
        if job_obj.minage <= user.age <= job_obj.maxage:
            score += min(job_obj.maxage - user.age, user.age - job_obj.minage)
        elif user.age < job_obj.minage:
            score += user.age - job_obj.minage
        elif user.age > job_obj.maxage:
            score += job_obj.maxage - user.age

        score += 3 * len(set(user.skills).intersection(set(job_obj.skills))) - len(
            set(job_obj.skills).difference(set(user.skills))
        )

        if time_job == "FULLTIME":
            if user.timetype == "FULLTIME":
                score += 10
            elif user.timetype == "PARTTIME":
                score += 5
            elif user.timetype == "PROJECT":
                score += 4

        elif time_job == "PARTTIME":
            if user.timetype == "FULLTIME":
                score += 5
            elif user.timetype == "PARTTIME":
                score += 10
            elif user.timetype == "PROJECT":
                score += 5

        elif time_job == "PROJECT":
            if user.timetype == "FULLTIME":
                score += 4
            elif user.timetype == "PARTTIME":
                score += 5
            elif user.timetype == "PROJECT":
                score += 10

        score += floor(1000 / (max(abs(user.salary - job_obj.salary), 1)))
        score = (score * 1000) + job
        job_score = job, score
        user.score.append(job_score)

    sorted_user_scores = sorted(user.score, key=lambda x: x[1], reverse=True)

    string_sorted_user_scores = ""

    if len(sorted_user_scores) <= 5:
        for item in sorted_user_scores:
            string_sorted_user_scores += f"({item[0]},{item[1]})"
    elif len(sorted_user_scores) > 5:
        for x in range(5):
            string_sorted_user_scores += (
                f"({sorted_user_scores[x][0]},{sorted_user_scores[x][1]})"
            )

    return string_sorted_user_scores


s = int(input())
skills = input().split()
q = int(input())

for x in range(q):
    try:
        command, *data = input().split()

        if command == "ADD-JOB":
            job = Job(*data)
            print(f"job id is {job.id}")

        elif command == "ADD-USER":
            user = User(*data)
            print(f"user id is {user.id}")

        elif command == "ADD-JOB-SKILL":
            add_job_skill(*data)
            print("skill added")

        elif command == "ADD-USER-SKILL":
            add_user_skill(*data)
            print("skill added")

        elif command == "VIEW":
            view(*data)
            print("tracked")

        elif command == "JOB-STATUS":
            print(Job.get(int(*data)))

        elif command == "USER-STATUS":
            print(User.get(int(*data)))

        elif command == "GET-JOBLIST":
            print(get_job(*data))

    except BaseException as e:
        print(e)

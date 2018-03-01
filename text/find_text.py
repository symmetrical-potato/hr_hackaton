import elasticsearch as esearch

es = esearch.Elasticsearch()


def find_by_string(string):
    '''
    Поиск по строке во всех дипломах и всех вакансих по строке (сейчас только по дипломам)
    :param string:
    :return: топ-10 результатов наиболее совпадающие по этому запросу
    [
        {
            'type': 'vacancy/document'
            'id': int
            'title': str
            'link' : str
        }, ...
    ]
    '''
    quer = { 
        'query':  
        {
            'match' : 
            {
                'text' : string,
            }
        }
    }
    res = []
    
    cur = es.search(index='uni', doc_type='diploma', body=quer)
    for hit in cur['hits']['hits']:
        res.append({'id'    : int(hit['_id']),
                   'score' : hit['_score'],
                   'title' : hit['_source']['title'],
                   'link'  : hit['_source']['link']})
        
    return res


def find_by_supervisor(supervisor):
    '''
    Все работы студентов с определенным научником
    :param supervisor str: фио научника
    :return: всес студенты определенного научника
        [
            {
                'student_name': str,
                'student_id': int
                'theme_name': str
            }, ...
        ]
    '''
    pass


def find_students_by_theme(theme_name):
    '''
    Поиск наиболее подходящих студентов по теме работодателя
    :arg theme_name string
    :return: top-5 students sorted by distance
        [
                {
                    'student_name': str, фио студента
                    'student_id': integer,
                    'rating': float, нормированное число
                }, ...
            ]
    '''
    pass


def find_vacancy_by_student(student_name):
    '''
    Поиск наиболее подходящих вакансий для студента
    :param student_name string: фио
    :return:top-5 vacancies sorted by distance
        [
            {
                'vacancy_name': str,
                'vacancy_id': integer,
                'rating': float
            }, ...
        ]
    '''
    pass


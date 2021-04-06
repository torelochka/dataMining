import numpy

from matrix_generator import matrix_from_graph


def summary_page_rank(matrix, height, G_LIST):
    n = height
    POW = 20

    beta = 0.85
    k = (1 - beta) / n

    M_matrix = matrix

    # Создаем вектор v
    v_vector = numpy.matrix([1 / n for i in range(height)])

    # Возводим в степень нашу матрицу и вектор умножаем на нее
    M_matrix_powed = M_matrix
    # v_vector.dot(M_matrix_powed)
    for i in range(POW):
        M_matrix_powed.dot(M_matrix)

    M_matrix_final = v_vector.dot(M_matrix_powed)

    MATRIX_RESULT_MxV = M_matrix_final.dot(beta)

    # Создаем единичную матрицу
    e = numpy.ones(height)

    e = e.dot(k)

    result = MATRIX_RESULT_MxV + e

    # Выводим полученную матрицу PageRank
    print(result)

    # Вывод топ 5 ссылок
    get_top(result, G_LIST, 5)


def get_top(result, G_list, top):
    a_ = numpy.sort(result).tolist()[0]

    a_ = a_[-top:]
    b_ = numpy.argsort(result).tolist()[0][-top:]
    G_list = list(G_list)
    arr = []
    for i in range(top):
        arr.append(
            f"{top - i} {a_[i]} {G_list[b_[i]]}"
        )

    print('result page rank')
    print(result.sum())

    print('----------')
    print('top', top)
    for i in arr:
        print(i)




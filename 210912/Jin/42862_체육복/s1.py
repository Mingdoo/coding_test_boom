def solution(n, lost, reserve):
    m_lst = [1] * n
    for i in range(n):
        if i + 1 in lost:
            m_lst[i] -= 1
        if i + 1 in reserve:
            m_lst[i] += 1

    if m_lst[1] == 2 and m_lst[0] == 0:
        m_lst[0] = 1
        m_lst[1] = 1

    for j in range(1, n - 1):
        if m_lst[j] == 0:
            try:
                if m_lst[j - 1] == 2:
                    m_lst[j] += 1
                    m_lst[j - 1] -= 1

                else:
                    if m_lst[j + 1] == 2:
                        m_lst[j] += 1
                        m_lst[j + 1] -= 1

            except:
                if n == 2:
                    if m_lst[0] == 2:
                        return 2

    if m_lst[n - 1] == 0:
        if m_lst[n - 2] == 2:
            m_lst[n - 1] = 1
            m_lst[n - 2] = 1

    for k in range(1, n - 1):
        if m_lst[k] == 2:
            if not m_lst[k - 1]:
                m_lst[k] = 1
                m_lst[k - 1] = 1

            else:
                if not m_lst[k + 1]:
                    m_lst[k] = 1
                    m_lst[k - 1] = 1

    answer = 0
    for k in m_lst:
        if k >= 1:
            answer += 1

    return answer
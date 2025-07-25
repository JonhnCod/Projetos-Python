def maior_primo(numero):
    if numero < 2:
        return None

    def e_primo(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

    for i in range(numero, 1, -1):
        if e_primo(i):
            return i

    return None

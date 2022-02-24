#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Snippet para calcular el numero de primos hasta n integrando R con Python

Script creado para la asignatura de Fundamentos de Python de la Escuela Internacional de Postgrados

Uso: python3 vlm_rprimo.py

@autor: Víctor Luque Martín
@fecha: 24-02-2022
@versión: 1.0
@licencia: GNU GPLv3
@email: victorluque341@gmail.com
"""
import rpy2.robjects as ro

def rprimo(n:int) -> ro.vectors.FloatVector:
    """
    Función principal del script

    Características:
    - Recibe un número entero positivo n como parámetro
    - Calcula el número de primos hasta n utilizando R
    - Retorna el número de primos hasta n

    :param n: número entero positivo
    :type n: int
    :return: número de primos hasta n
    :rtype: ro.vectors.FloatVector
    """

    # Codigo R con la función de para calcular números primos
    codigo_r = '''
        primos <- function(n){
            n <- as.integer(n)
            if(n < 2)
                return(0)
            else
                primes <- c(2)
                for(i in 2:n){
                is_prime <- TRUE
                for(j in primes){
                    if(i %% j == 0){
                    is_prime <- FALSE
                    break
                    }
                }
                if(is_prime)
                    primes <- c(primes, i)
                }
            return(primes)
        }
    '''
    # Se importa el codigo R
    ro.r(codigo_r)
    # Se llama a la función de R
    primos = ro.globalenv['primos']
    return primos(n)
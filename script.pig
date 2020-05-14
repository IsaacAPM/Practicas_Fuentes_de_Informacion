-- FOREACH anidado
A = LOAD 'votacion.csv' USING PigStorage(',') AS (hora:int, gen:chararray, dist:int, cand:chararray);
gH = GROUP A BY hora;
hist = FOREACH gH GENERATE group,COUNT(A);
STORE hist INTO 'SolucionFOREACHanidado/histograma';
M = GROUP hist ALL;
max_min = FOREACH M GENERATE MIN(hist.$1), MAX(hist.$1);
STORE max_min INTO 'SolucionFOREACHanidado/max_min';

-- SPLIT
SPLIT A INTO cMujer IF cand == 'CAND1' OR cand == 'CAND3',
    cHombre IF cand == 'CAND2' OR cand == 'CAND4' OR cand == 'CAND5';
votMujeres = GROUP cMujer BY cand;
nVotMujeres = FOREACH votMujeres GENERATE group,COUNT($1);
votHombres = GROUP cHombre BY cand;
nVotHombres = FOREACH votHombres GENERATE group,COUNT($1);
STORE nVotMujeres INTO 'SolucionSPLIT/nVotMujeres';
STORE nVotHombres INTO 'SolucionSPLIT/nVotHombres';

-- JOIN
encuestas = LOAD 'Encuestas.csv' USING PigStorage(',') as (cand:chararray,casa:chararray,valor:int);
CandYEnc = JOIN A BY cand, encuestas BY cand;
CandYPorc = FOREACH CandYEnc GENERATE A::cand, encuestas::valor;
ConocPorCand = GROUP CandYPorc by cand;
avgConocCand = FOREACH ConocPorCand GENERATE group, AVG(CandYPorc.valor);
STORE avgConocCand INTO 'SolucionJOIN';

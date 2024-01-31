function x = Tridiag(A, d)

    % This function solves a tridiagonal linear system of the form Ax = d
    % using the Thomas algorithm

    % Calculate size of the system
    N = length(d);

    % Determine lower, main and upper diagonal elements
    a = [0; diag(A, -1)];
    b = diag(A);
    c = [diag(A, 1); 0];

    % Forward sweep
    c(1) = c(1) / b(1);
    d(1) = d(1) / b(1);

    for i = 2:N
        c(i) = c(i) / (b(i) - a(i) * c(i - 1));
        d(i) = (d(i) - a(i) * d(i - 1)) / (b(i) - a(i) * c(i - 1));
    end

    % Backward sweep
    x(N) = d(N);

    for i = N - 1:-1:1
        x(i) = d(i) - c(i) * x(i + 1);
    end

end

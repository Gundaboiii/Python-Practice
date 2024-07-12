import sys
import pandas as pd
import time


class SudokuSolver:
    def __init__(self, puzzle):
        self.puzzle = puzzle
        self.size = len(puzzle)
        self.box_size = int(self.size ** 0.5)
        self.nodes_generated = 0
        self.domain = {str(i) for i in range(1, self.size + 1)}

    def is_valid(self, row, col, num):
        if num in self.puzzle[row]:
            return False

        for r in range(self.size):
            if self.puzzle[r][col] == num:
                return False

        box_row_start = (row // self.box_size) * self.box_size
        box_col_start = (col // self.box_size) * self.box_size
        for r in range(box_row_start, box_row_start + self.box_size):
            for c in range(box_col_start, box_col_start + self.box_size):
                if self.puzzle[r][c] == num:
                    return False

        return True

    def solve_brute_force(self):
        empty_cell = self.find_empty()
        if not empty_cell:
            return True

        row, col = empty_cell
        for num in self.domain:
            if self.is_valid(row, col, num):
                self.puzzle[row][col] = num
                self.nodes_generated += 1

                if self.solve_brute_force():
                    return True

                self.puzzle[row][col] = 'X'

        return False

    def backtrack(self):
        empty_cell = self.find_empty()
        if not empty_cell:
            return True

        row, col = empty_cell
        for num in self.domain:
            if self.is_valid(row, col, num):
                self.puzzle[row][col] = num
                self.nodes_generated += 1

                if self.backtrack():
                    return True

                self.puzzle[row][col] = 'X'

        return False

    def solve_forward_checking_mrv(self):
        empty_cell = self.select_unassigned_variable()
        if not empty_cell:
            return True

        row, col = empty_cell
        valid_values = self.get_valid_values(row, col)
        for value in sorted(valid_values, key=lambda x: self.count_conflicts(row, col, x)):
            self.puzzle[row][col] = value
            self.nodes_generated += 1

            if self.solve_forward_checking_mrv():
                return True

            self.puzzle[row][col] = 'X'

        return False

    def find_empty(self):
        for r in range(self.size):
            for c in range(self.size):
                if self.puzzle[r][c] == 'X':
                    return r, c
        return None

    def select_unassigned_variable(self):
        min_remaining_values = float('inf')
        selected_var = None
        for i in range(self.size):
            for j in range(self.size):
                if self.puzzle[i][j] == 'X':
                    remaining_values = len(self.get_valid_values(i, j))
                    if remaining_values < min_remaining_values:
                        min_remaining_values = remaining_values
                        selected_var = (i, j)
        return selected_var

    def get_valid_values(self, row, col):
        valid_values = self.domain.copy()
        for i in range(self.size):
            if self.puzzle[row][i] in valid_values:
                valid_values.remove(self.puzzle[row][i])
            if self.puzzle[i][col] in valid_values:
                valid_values.remove(self.puzzle[i][col])

        box_row_start = (row // self.box_size) * self.box_size
        box_col_start = (col // self.box_size) * self.box_size
        for r in range(box_row_start, box_row_start + self.box_size):
            for c in range(box_col_start, box_col_start + self.box_size):
                if self.puzzle[r][c] in valid_values:
                    valid_values.remove(self.puzzle[r][c])

        return valid_values

    def count_conflicts(self, row, col, value):
        count = 0
        self.puzzle[row][col] = value
        for i in range(self.size):
            if i != col and self.puzzle[row][i] == value:
                count += 1
            if i != row and self.puzzle[i][col] == value:
                count += 1

        box_row_start = (row // self.box_size) * self.box_size
        box_col_start = (col // self.box_size) * self.box_size
        for r in range(box_row_start, box_row_start + self.box_size):
            for c in range(box_col_start, box_col_start + self.box_size):
                if (r != row or c != col) and self.puzzle[r][c] == value:
                    count += 1

        self.puzzle[row][col] = 'X'
        return count

    def test_sudoku_solution(self):
        for row in self.puzzle:
            if 'X' in row:
                return False
            if sorted(row) != [str(i) for i in range(1, self.size + 1)]:
                return False
        return True


def print_board(board):
    for row in board:
        print(','.join(str(num) if num != 'X' else 'X' for num in row))
def read_sudoku_from_csv(filename):
    df = pd.read_csv(filename, header=None)
    puzzle = df.values.tolist()
    return puzzle


def save_sudoku_to_csv(filename, puzzle):
    df = pd.DataFrame(puzzle)
    df.to_csv(filename, index=False, header=False)


def main(mode, filename):
    if mode not in ['1', '2', '3', '4']:
        print("ERROR: Invalid mode. Mode must be 1, 2, 3, or 4.")
        sys.exit(1)

    try:
        puzzle = read_sudoku_from_csv(filename)
    except FileNotFoundError:
        print(f"ERROR: File '{filename}' not found.")
        sys.exit(1)
    print("Dhingra, Ronak, A20531917 solution:")
    print(f"Input file: {filename}")
    print("Input puzzle:")
    print_board(puzzle)
    #print(f"Algorithm: {algorithm_name}\n")
    solver = SudokuSolver(puzzle)
    start_time = time.time()


    if mode == '1':
        solver.solve_brute_force()
        algorithm_name = "Brute Force"
    elif mode == '2':
        solver.backtrack()  # Use backtracking CSP for mode 2
        algorithm_name = "Constraint Satisfaction Problem (Backtracking)"
    elif mode == '3':
        solver.solve_forward_checking_mrv()
        algorithm_name = "CSP with Forward Checking and MRV Heuristics"
    elif mode == '4':
        if solver.test_sudoku_solution():
            print("This is a valid, solved, Sudoku puzzle.")
        else:
            print("ERROR: This is NOT a solved Sudoku puzzle.")
        return

    solve_time = time.time() - start_time

    print(f"Algorithm: {algorithm_name}\n")
    print(f"Number of search tree nodes generated: {solver.nodes_generated}")
    print(f"Search time: {solve_time:.4f} seconds\n")
    print("Output puzzle:")
    print_board(puzzle)
    print()
    output_filename = filename.replace('.csv', '_SOLUTION.csv')
    save_sudoku_to_csv(output_filename, solver.puzzle)
    print(f"Solved puzzle saved to {output_filename}")


if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("ERROR: Not enough/too many input arguments.")
        sys.exit(1)

    mode = sys.argv[1]
    filename = sys.argv[2]

    main(mode, filename)

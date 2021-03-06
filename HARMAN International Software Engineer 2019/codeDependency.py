def dependency_check(code_id):
    visited = set([])
    dependency_list = []
    topological_sort(code_id, dependency_list)
    return dependency_list


def topological_sort(parent_code_id):
    if code_id in visited:
        return

    visited.add(code_id)
    seen.add(parent_code_id)

    for child_code_id in parent_code_id.children:
        if child_code_id in seen:
            print("Cyclic dependency present")
        topological_sort(code_id)

    seen.remove(parent_code_id)
    dependency_list.append(parent_code_id)

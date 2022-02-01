from src.database import crud

def get_exercise_templates(root: 'WorkoutTemplate'):
    return crud.get_exercise_templates(root.id)

def get_workout_template(root: 'Workout'):
    return crud.get_workout_template(root.workout_template_id)

def get_exercise_template(root: 'Exercise'):
    return crud.get_exercise_template(root.exercise_template_id)

def get_exercises(root: 'Workout'):
    return crud.get_exercises(root.id)

def get_sets(root: 'Exercise'):
    return crud.get_sets(root.id)

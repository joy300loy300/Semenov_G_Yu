from django.shortcuts import render, redirect, get_object_or_404
from .models import Group, Student, Grade, Subject
from .forms import GroupForm, StudentForm, GradeForm, SubjectForm


def index(request):
    groups = Group.objects.all()
    subjects = Subject.objects.all()

    group_stats = []
    for group in groups:
        subject_averages = {}
        for subject in subjects:
            avg = group.get_average_grade_by_subject(subject)
            subject_averages[subject] = avg
        group_stats.append({
            'group': group,
            'overall_average': group.get_average_grade(),
            'subject_averages': subject_averages
        })

    return render(request, 'index.html', {
        'group_stats': group_stats,
        'subjects': subjects,
    })


def group_list(request):
    groups = Group.objects.all()
    return render(request, 'groups/list.html', {'groups': groups})


def group_create(request):
    form = GroupForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('group_list')
    return render(request, 'groups/form.html', {'form': form})


def group_update(request, pk):
    group = get_object_or_404(Group, pk=pk)
    form = GroupForm(request.POST or None, instance=group)
    if form.is_valid():
        form.save()
        return redirect('group_list')
    return render(request, 'groups/form.html', {'form': form})


def group_delete(request, pk):
    group = get_object_or_404(Group, pk=pk)
    if request.method == 'POST':
        group.delete()
        return redirect('group_list')
    return render(request, 'groups/confirm_delete.html', {'object': group})


def student_list(request):
    students = Student.objects.select_related('group').all()
    return render(request, 'students/list.html', {'students': students})


def student_create(request):
    form = StudentForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('student_list')
    return render(request, 'students/form.html', {'form': form})


def student_update(request, pk):
    student = get_object_or_404(Student, pk=pk)
    form = StudentForm(request.POST or None, instance=student)
    if form.is_valid():
        form.save()
        return redirect('student_list')
    return render(request, 'students/form.html', {'form': form})


def student_delete(request, pk):
    student = get_object_or_404(Student, pk=pk)
    if request.method == 'POST':
        student.delete()
        return redirect('student_list')
    return render(request, 'students/confirm_delete.html', {'object': student})


def grade_list(request):
    grades = Grade.objects.select_related('student').all()
    return render(request, 'grades/list.html', {'grades': grades})


def grade_create(request):
    form = GradeForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('grade_list')
    return render(request, 'grades/form.html', {'form': form})


def grade_update(request, pk):
    grade = get_object_or_404(Grade, pk=pk)
    form = GradeForm(request.POST or None, instance=grade)
    if form.is_valid():
        form.save()
        return redirect('grade_list')
    return render(request, 'grades/form.html', {'form': form})


def grade_delete(request, pk):
    grade = get_object_or_404(Grade, pk=pk)
    if request.method == 'POST':
        grade.delete()
        return redirect('grade_list')
    return render(request, 'grades/confirm_delete.html', {'object': grade})


def subject_list(request):
    subjects = Subject.objects.all()
    return render(request, 'subjects/list.html', {'subjects': subjects})


def subject_create(request):
    if request.method == 'POST':
        form = SubjectForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('subject_list')
    else:
        form = SubjectForm()
    return render(request, 'subjects/form.html', {'form': form, 'title': 'Добавить предмет'})


def subject_update(request, pk):
    subject = get_object_or_404(Subject, pk=pk)
    if request.method == 'POST':
        form = SubjectForm(request.POST, instance=subject)
        if form.is_valid():
            form.save()
            return redirect('subject_list')
    else:
        form = SubjectForm(instance=subject)
    return render(request, 'subjects/form.html', {'form': form, 'title': 'Изменить предмет'})


def subject_delete(request, pk):
    subject = get_object_or_404(Subject, pk=pk)
    if request.method == 'POST':
        subject.delete()
        return redirect('subject_list')
    return render(request, 'subjects/confirm_delete.html', {'subject': subject})

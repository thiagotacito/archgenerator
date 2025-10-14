from archgenerator.generators.python_generator import PythonGenerator
from archgenerator.generators.csharp_generator import CSharpGenerator

def run():
    language = input("Choose langauge (csharp/python): ").strip().lower()
    project_name = input("Enter project name: ").strip()

    if language == "python":
        generator = PythonGenerator(project_name)
    elif language == "csharp":
        generator = CSharpGenerator(project_name)
    else:
        print("Unsupported language.")
        return
    
    generator.generate()
    print(f"{language.capitalize()} project '{project_name}' generated successfully.")

if __name__ == "__main__":
    run()
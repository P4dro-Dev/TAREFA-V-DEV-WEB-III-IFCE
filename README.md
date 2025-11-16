##  📋| StudyTasks — Sistema Django com Banco de Dados (Tarefa 5)

Este repositório contém uma aplicação web desenvolvida em Django, implementando um sistema completo de gerenciamento de autores com mapeamento objeto-relacional (ORM). O projeto cumpre todos os requisitos solicitados na atividade, incluindo criação de modelo, CRUD, buscas, templates, admin, branch Git e documentação.

## 📌 Objetivo do Projeto

Criar uma aplicação Django utilizando um modelo de dados personalizado e o ORM para operações de:

```
Inserir registros

Listar e buscar dados

Editar registros

Excluir registros

Integrar o modelo ao Admin do Django
```

Além disso, cumprir os requisitos do Git: criação da branch banco-de-dados, commits, push e merge.

## 🗂️ Estrutura do Projeto

```
studytasks_project/
│
├── Relatório_PDF_IMG's+Descrição+ID
├── coreapp/
│   ├── models.py
│   ├── views.py
│   ├── forms.py
│   ├── admin.py
│   ├── urls.py
│   └── templates/
│       ├── base.html
│       ├── autor_list.html
│       ├── autor_form.html
│       ├── autor_detail.html
│       └── autor_confirm_delete.html
│
├── studytasks_project/
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
│
├── manage.py
├── README.md

```

## 🧩 Modelo de Dados

O sistema utiliza a classe Autor, definida assim:

class Autor(models.Model):
    nome = models.CharField('Nome', max_length=200)
    email = models.EmailField('E-mail', blank=True, null=True)
    mini_curriculo = models.TextField('Mini currículo', blank=True)
    criado_em = models.DateTimeField('Criado em', auto_now_add=True)

    def __str__(self):
        return self.nome

## 🔧 Funcionalidades Implementadas (CRUD)


# ✔️ 1. Listagem de Autores
```
Página inicial /

Mostra todos os autores cadastrados

Inclui campo de busca por nome ou e-mail
```
# ✔️ 2. Cadastro de Autor
```
Página /autor/novo/

Formulário baseado em ModelForm
```
Insere registro no banco

# ✔️ 3. Busca
```
Implementada via QuerySet com icontains

Feita diretamente na listagem
```
# ✔️ 4. Edição
```
Página /autor/<id>/editar/

Carrega formulário com dados existentes
```
#✔️ 5. Exclusão
```
Página /autor/<id>/apagar/

Confirmação antes de excluir o registro
```
# ✔️ 6. Detalhamento
```
Página /autor/<id>/
```
🛠️ Integração com o Admin

O modelo Autor foi adicionado ao Django Admin:
```
@admin.register(Autor)
class AutorAdmin(admin.ModelAdmin):
    list_display = ('nome', 'email', 'criado_em')
    search_fields = ('nome', 'email')
```

Assim, é possível gerenciar autores pelo painel administrativo em:

```
/admin/
```

## 🌿 Git — Branch, Commits e Merge

Para atender aos requisitos de versionamento da atividade, seguem os comandos utilizados:

```
# Criar a branch da atividade
git checkout -b banco-de-dados

# Adicionar os arquivos da atividade
git add .

# Commit da implementação
git commit -m "Implementa modelo Autor, CRUD e templates"

# Envio da branch para o GitHub
git push -u origin banco-de-dados

# Após revisão, mesclar na main
git checkout main
git pull origin main
git merge banco-de-dados
git push origin main
```

## ▶️ Como Executar o Projeto

```
1. Criar ambiente virtual
python -m venv venv

2. Ativar o ambiente

Windows

venv\Scripts\activate


Linux/Mac

source venv/bin/activate

3. Instalar dependências
pip install -r requirements.txt

4. Criar o banco de dados
python manage.py makemigrations
python manage.py migrate

5. Criar superusuário (opcional)
python manage.py createsuperuser

6. Executar o servidor
python manage.py runserver

7. Acessar no navegador
```

```
Aplicação: http://127.0.0.1:8000/
```
Admin: http://127.0.0.1:8000/admin/
```

# This template is used inside of member.py
TEMPLATE = """
{%- if node.has(visibility, kinds, static) -%}
{%- if parent is none -%}
## {{title}}
{%- else -%}
## {{title}} inherited from {{node.name}}

See [{{node.name_long}}]({{node.url}})
{%- endif %}

| Type | Name |
| ---: | :--- |
{% for member in node.query(visibility, kinds, static) -%}
{%- if member.is_group -%}
| module | [**{{member.title}}**]({{link_prefix}}{{member.url}}) {{member.suffix}}<br>{{member.brief}} |
{%- elif member.is_file -%}
| file | [**{{member.name_short}}**]({{link_prefix}}{{member.url}}) {{member.suffix}}<br>{{member.brief}} |
{%- elif member.is_dir -%}
| dir | [**{{member.name_short}}**]({{link_prefix}}{{member.url}}) {{member.suffix}}<br>{{member.brief}} |
{%- elif member.is_namespace -%}
| {{member.kind.value}} | [**{{member.name_long if node.is_group else member.name_short}}**]({{link_prefix}}{{member.url}}) {{member.suffix}}<br>{{member.brief}} |
{%- elif member.is_class or member.is_interface or member.is_struct -%}
| {{member.kind.value}} | [**{{member.name_long if node.is_group else member.name_short}}**]({{link_prefix}}{{member.url}}) {{member.suffix}}<br>{{member.brief}} |
{%- elif member.is_enum or member.is_function or member.is_variable or member.is_union or member.is_typedef -%}
| {{member.prefix}} {{member.type}} | [**{{member.name_long if node.is_group else member.name_short}}**]({{link_prefix}}{{member.url}}) {{member.params}} {{member.suffix}}<br>{{member.brief}} |
{%- else -%}
| {{member.prefix}} {{member.type}} | [**{{member.name_long if node.is_group else member.name_short}}**]({{link_prefix}}{{member.url}}) {{member.params}} {{member.suffix}}<br>{{member.brief}} |
{%- endif %}
{% endfor -%}

{%- endif -%}
"""

from assignment_function import open_ai,reads_file,wp_paragraph,wp_h2,headers,wp_images
from requests import post


heading_lists = reads_file('C:/Users/hp/Desktop/python_practice/Day_28/kids_bicycle.txt')
end_line = ' write a paragraph about'
dictionary = {}
for heading in heading_lists :
    command = f'{end_line} {heading}'
    answer = open_ai(command)
    print(answer)
    dictionary[heading] = answer

ttle = 'bicycle for kids'
content = ''
for key, value in dictionary.items():
    wp_img1 = wp_images('https://cyclist.b-cdn.net/sites/cyclist/files/2022/12/cyclist_junior_kids_bike_patrik_lundin_.jpg',ttle)
    heading = wp_h2(key)
    paragraph = wp_paragraph(value)
    temp = wp_img1 + heading + paragraph
    content += temp

title = open_ai(f'write a seo-friedly title for {ttle}')
slugs = title.lower().strip().replace(' ','-')


wp_data = {

    'title'     : title,
    'slug'      : slugs,
    'content'   : content,
    'categories': '15',
    'status'    : 'publish'
}


wp_header = headers('Mohammad')
wp_endpoints = 'https://dev-moprojects.pantheonsite.io/wp-json/wp/v2/posts'
post(wp_endpoints, data = wp_data, headers = wp_header)


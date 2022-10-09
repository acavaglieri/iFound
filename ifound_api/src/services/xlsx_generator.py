from src.cruds import users as u_cruds
from src.schemas import users as u_schemas
from datetime import datetime
from sqlalchemy.orm import Session
import xlsxwriter


def create_xlsx_file_for_users(db: Session, filter: u_schemas.UsersFilter):

    filename = 'users-list{}.xlsx'.format(str(datetime.today()))
    workbook = xlsxwriter.Workbook('/tmp/{}'.format(filename))
    worksheet = workbook.add_worksheet()
    header = workbook.add_format({'bold': True, 'bg_color': '#9fedb4', 'align': 'center', 'valign': 'middle', 'border': True})
    body_cell = workbook.add_format({'border': True, 'align': 'center', 'valign': 'middle'})
    

    users = u_cruds.get_users(db, filter)[0]

    worksheet.set_column(1, 20, 50)

    worksheet.write('A1', 'ID', header)
    worksheet.write('B1', 'Nome', header)
    worksheet.write('C1', 'Email', header)
    worksheet.write('D1', 'Celular', header)
    worksheet.write('E1', 'Nascimento', header)
    worksheet.write('F1', 'CPF', header)
    worksheet.write('G1', 'Permissões', header)
    worksheet.write('H1', 'Logradouro', header)
    worksheet.write('I1', 'Número', header)
    worksheet.write('J1', 'Bairro', header)
    worksheet.write('K1', 'Cidade', header)
    worksheet.write('L1', 'CEP', header)
    worksheet.write('M1', 'Estado', header)
    worksheet.write('N1', 'País', header)
    worksheet.write('O1', 'Criado em', header)
    worksheet.write('P1', 'Atualizado em', header)

    row = 1
    col = 0

    for val in users:

        worksheet.write(row, col, val.id, body_cell)
        worksheet.write(row, col +1, str(val.name), body_cell)
        worksheet.write(row, col +2, str(val.email), body_cell)
        worksheet.write(row, col +3, str(val.cellphone), body_cell)
        worksheet.write(row, col +4, str(val.birthday.strftime('%d/%m/%Y')), body_cell)
        worksheet.write(row, col +5, str(val.federal_id), body_cell)
        worksheet.write(row, col +6, str(val.role), body_cell)
        worksheet.write(row, col +7, str(val.address), body_cell)
        worksheet.write(row, col +8, str(val.house_number), body_cell)
        worksheet.write(row, col +9, str(val.quarter), body_cell)
        worksheet.write(row, col +10, str(val.city), body_cell)
        worksheet.write(row, col +11, str(val.zip_code), body_cell)
        worksheet.write(row, col +12, str(val.state), body_cell)
        worksheet.write(row, col +13, str(val.country), body_cell)
        worksheet.write(row, col +14, str(val.created_at.strftime('%d/%m/%Y')), body_cell)
        worksheet.write(row, col +15, str(val.updated_at.strftime('%d/%m/%Y')), body_cell)
        row += 1
    
    workbook.close()
    return filename
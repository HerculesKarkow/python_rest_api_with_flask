from flask_restful import Resource, reqparse

hoteis = [
    {
        'hotel_id': 'bravo',
        'nome': 'teste',
        'estrelas': 'estrelas teste',
        'diaria': 300.00,
        'cidade': 'trssasas'
    },
    {
        'hotel_id': 'nasasas',
        'nome': 'assasas',
        'estrelas': 'asasasasas',
        'diaria': 300.00,
        'cidade': 'asasaasa'
    }
]


class Hoteis(Resource):
    def get(self):
        return {'hoteis': hoteis}


class Hotel(Resource):
    arguments = reqparse.RequestParser()
    arguments.add_argument('nome')
    arguments.add_argument('estrelas')
    arguments.add_argument('diaria')
    arguments.add_argument('cidade')

    def find_hotel(hotel_id):
        for hotel in hoteis:
            if hotel['hotel_id'] == hotel_id:
                return hotel
        return None

    def get(self, hotel_id):
        hotel = Hotel.find_hotel(hotel_id)
        if hotel:
            return hotel
        return {'message': 'Hotel not found!'}, 404

    def post(self, hotel_id):

        dados = Hotel.arguments.parse_args()

        novo_hotel = {
            'hotel_id': hotel_id,
            'nome': dados['nome'],
            'estrelas': dados['estrelas'],
            'diaria': dados['diaria'],
            'cidade': dados['cidade']
        }

        hoteis.append(novo_hotel)
        return novo_hotel, 200

    def put(self, hotel_id):

        dados = Hotel.arguments.parse_args()

        novo_hotel = {'hotel_id': hotel_id, **dados}

        hotel = Hotel.find_hotel(hotel_id)

        if hotel:
            hotel.update(novo_hotel)

        hoteis.append(novo_hotel)

        return novo_hotel

    def delete(self, hotel_id):
        pass

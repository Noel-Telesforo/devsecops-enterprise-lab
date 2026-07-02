from flask import Blueprint, jsonify, request

main_bp = Blueprint('main', __name__)

@main_bp.route('/', methods=['GET'])
def home():
    """Página principal"""
    return jsonify({
        'message': 'DevSecOps Enterprise Lab',
        'version': '1.0.0',
        'status': 'running'
    })

@main_bp.route('/health', methods=['GET'])
def health():
    """Health check para monitoreo"""
    return jsonify({'status': 'healthy'}), 200

@main_bp.route('/api/v1/users', methods=['GET'])
def get_users():
    """Endpoint de ejemplo para usuarios"""
    users = [
        {'id': 1, 'name': 'Alice'},
        {'id': 2, 'name': 'Bob'},
        {'id': 3, 'name': 'Charlie'}
    ]
    return jsonify({'users': users})

@main_bp.route('/api/v1/users', methods=['POST'])
def create_user():
    """Crear un nuevo usuario"""
    data = request.get_json()
    if not data or 'name' not in data:
        return jsonify({'error': 'Name is required'}), 400
    
    # Simulamos creación
    new_user = {
        'id': 4,
        'name': data['name']
    }
    return jsonify(new_user), 201
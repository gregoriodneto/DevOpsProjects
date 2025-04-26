import subprocess
import os
from dotenv import load_dotenv

load_dotenv()

DOCKER_USERNAME = os.getenv("DOCKER_USERNAME")

SERVICES = {
    "go-service": "./go-service",
    "python-service": "./python-service",
    "nginx": "nginx"
}

K8S_MANIFESTS = [
    "./k8s/go-deployment.yaml",
    "./k8s/python-deployment.yaml",
    "./k8s/nginx-deployment.yaml",
    "./k8s/nginx-service.yaml"
]

def run_command(cmd, cwd=None):
    print(f"👉 Executando: {cmd}")
    result = subprocess.run(cmd, shell=True, cwd=cwd)
    if result.returncode != 0:
        raise RuntimeError(f"❌ Erro ao executar: {cmd}")
    
def create_kind_cluster():
    print("\n🔧 Criando cluster Kind...")
    run_command("kind delete cluster --name meu-cluster || true")
    run_command("kind create cluster --name meu-cluster --config ./k8s/kind-config.yaml")
    
def env_k8s():
    os.environ["DOCKER_USERNAME"] = DOCKER_USERNAME
    for manifest in K8S_MANIFESTS:
        os.system(f"envsubst < {manifest}.template | kubectl apply -f -")
    
def build_and_push_images():
    for service, path in SERVICES.items():
        image = f"{DOCKER_USERNAME}/{service}:latest"
        print(f"\n🔨 Buildando imagem {image}...")
        run_command(f"docker build -t {image} .", cwd=path)

        print(f"📤 Fazendo push da imagem {image}...")
        run_command(f"docker push {image}")

def apply_k8s_manifests():
    for manifest in K8S_MANIFESTS:
        print(f"\n🚀 Aplicando manifest {manifest}...")
        run_command(f"kubectl apply -f {manifest}")

def main():
    print("🚧 Iniciando deploy completo...\n")
    env_k8s()
    build_and_push_images()
    create_kind_cluster()
    apply_k8s_manifests()
    print("\n✅ Deploy finalizado com sucesso!")

if __name__ == "__main__":
    main()
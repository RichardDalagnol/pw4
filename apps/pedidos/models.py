from django.db import models
from django.urls import reverse


class Item(models.Model):
    pedido = models.ForeignKey("pedidos.Pedido", verbose_name="Pedido", on_delete=models.CASCADE)
    produto = models.ForeignKey("produtos.Produto", verbose_name="Produto", on_delete=models.CASCADE)
    quantidade = models.DecimalField("Quantidade", max_digits=5, decimal_places=2)
    valor_base = models.DecimalField("Valor base", max_digits=10, decimal_places=2)
    subtotal = models.DecimalField("Subtotal", max_digits=10, decimal_places=2)

    class Meta:
        verbose_name = "Item"
        verbose_name_plural = "Itens"

    def __str__(self):
        return "#" + str(self.pedido.id) + " - " + self.produto.nome

    def get_absolute_url(self):
        return reverse("pedidos__detail", kwargs={"pk": self.pedido.pk})

    def get_update_url(self):
        return reverse("pedidos__atualiza__item", kwargs={"pk": self.pk})

    def get_delete_url(self):
        return reverse("pedidos__excluir__item", kwargs={"pk": self.pk})


class Pedido(models.Model):
    CRIADO = "CRD"
    FECHADO = "FCD"
    ENVIADO = "EVD"
    STATUSES = [
        (CRIADO, "Criado"),
        (FECHADO, "Fechado"),
        (ENVIADO, "Enviado"),
    ]

    cliente = models.ForeignKey('clientes.Cliente', verbose_name='Cliente', on_delete=models.CASCADE)
    data = models.DateField(verbose_name="Data")
    criado = models.DateField(auto_now_add=True, verbose_name="Criado em", null=True)
    total = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Total", default=0.0)
    status = models.CharField(max_length=5, verbose_name="Status", choices=STATUSES, default=CRIADO)
    itens = models.ManyToManyField("produtos.Produto", verbose_name="Itens", through="pedidos.Item")

    class Meta:
        verbose_name = "Pedido"
        verbose_name_plural = "Pedidos"

    def __str__(self):
        return "#" + str(self.id) + " " + self.pedido.nome

    def get_absolute_url(self):
        return reverse("pedidos__detail", kwargs={"pk": self.pk})

    def get_itens(self):
        return Item.objects.filter(pedido=self.pk)

    def get_update_url(self):
        return reverse("pedido__atualiza", kwargs={"pk": self.pk})

    def get_add_item_url(self):
        return reverse("pedidos__add__item", kwargs={"pedido": self.pk})

    def get_delete_url(self):
        return reverse("pedidos__delete", kwargs={"pk": self.pk})

    def update_total(self):
        itens = self.get_itens()
        total = 0
        for item in itens:
            total = total + item.subtotal
        self.total = total
        self.save()

# Small-transformer federated LoRA canary reputation test

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `small-transformer-federated-lora-canary-reputation-test-0cdf7951bd`
Run ID: `small-transformer-federated-lora-canary-reputation-test-0cdf7951bd-20260630T153724458160+0000`

> This is a promising-signal record, not a paper. It is bounded local evidence preserved for possible larger-compute follow-up.

## Deterministic curation

- Bucket: Follow-up recommended
- Score: `83`
- Score breakdown: `{"bounded_evidence": 20, "evidence_strength": 25, "followup": 15, "hypothesis_status": 15, "source_lineage": 8}`

Reasons:
- moderate evidence_strength
- mixed hypothesis_status
- source lineage present
- bounded follow-up is specified
- local evidence artifact paths are present
- metrics artifact is present
- project decision artifact is present

## Source

- Parent run decision: Canary-verified reputation weighting for federated LoRA: enoch://control-plane/projects/canary-verified-reputation-weighting-for-federated-lora-b45287f36e60/runs/canary-verified-reputation-weighting-for-federated-lora-b45287f36e60-20260630T145933826069+0000
- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/5c910545da46

## What looked useful

Uncalibrated off-distribution canaries failed and slightly increased malicious weight (0.3339 reputation vs 0.3000 FedAvg) with no attack-success reduction. Calibrated canaries downweighted malicious clients under stress (0.0566 reputation vs 0.3000 FedAvg) while preserving clean accuracy, but FedAvg attack success was already 0.0, so no mitigation effect was demonstrated.

## Boundaries and scale limits

No real language-model corpus, no GPT-2-small-class baseline, no secure aggregation, no adaptive attacker, no heterogeneous real clients, and no multi-node federation. The calibrated positive signal was observed in a toy setup where FedAvg already had 0 attack success.

## Claim scope

Toy synthetic sequence-classification experiment with a 2-layer small transformer, frozen base weights, LoRA adapter federation, 10 clients, 3 malicious clients, 5 seeds, and server-held trigger canaries. Evidence supports only the scoped mechanism that calibrated clean canaries can rank and downweight malicious LoRA updates; it does not support a defense claim because attack success was not reduced versus FedAvg.

## Why it stopped

No-paper useful signal: the toy experiment produced mechanism evidence and an uncalibrated failure mode, but not a direct defense improvement over FedAvg.

## Recommended next action

Run a bounded harder follow-up where FedAvg demonstrably suffers a trigger attack before testing whether calibrated canary reputation reduces attack success.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Harder federated LoRA canary reputation test with nonzero FedAvg attack success
- Success threshold: Reputation aggregation cuts trigger attack success by at least 50% relative to FedAvg with no more than 2 percentage points clean-accuracy loss, and benign vs malicious canary losses remain separated in at least 4 of 5 seeds.
- Stop condition: Stop as negative if FedAvg cannot be made vulnerable under bounded local compute, or if reputation does not reduce attack success despite measurable malicious canary-loss separation.

## Evidence references

- Artifact root: `<local-path>/projects/small-transformer-federated-lora-canary-reputation-test-0cdf7951bd`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.

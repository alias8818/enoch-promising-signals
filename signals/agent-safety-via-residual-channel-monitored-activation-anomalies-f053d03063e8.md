# Agent Safety via Residual-Channel-Monitored Activation Anomalies

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `agent-safety-via-residual-channel-monitored-activation-anomalies-f053d03063e8`
Run ID: `agent-safety-via-residual-channel-monitored-activation-anomalies-f053d03063e8-20260524T230201024174+0000`

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

- Provider-backed Research Facility batch: hf:zai-org/GLM-5.1: enoch://research-facility/provider/hf:zai-org/GLM-5.1/2693334657a2

## What looked useful

The backdoored policy learned perfectly and harmful+trigger inputs produced unsafe compliance in all seeds, but residual-channel max-z anomaly monitoring was dominated by trigger/OOD rarity rather than safety-relevant behavior: harmful+trigger vs clean AUROC averaged 0.770, benign+trigger vs clean AUROC averaged 0.864, harmful+trigger vs benign+trigger AUROC averaged 0.241, and FPR at 95% TPR averaged 0.470.

## Boundaries and scale limits

Synthetic token task only; tiny randomly trained classifier; no natural-language prompts, pretrained LLM residual streams, real agent tool use, adaptive attacks, or comparison to learned activation probes.

## Claim scope

In a five-seed synthetic tiny-transformer backdoor proxy, max absolute residual-channel z-score monitoring detects some rare-trigger and OOD activation anomalies but does not isolate trigger-induced unsafe compliance from benign trigger presence.

## Why it stopped

Proxy experiment showed residual anomalies track rare trigger/OOD activation more than unsafe behavior; this is not full validation on real agents and is not paper-ready.

## Recommended next action

Stop this run as a no-paper useful signal: the simple residual-channel max-z monitor is an early proxy falsification for safety-specific detection, while a bounded follow-up should test contrastive residual monitors that condition on benign trigger controls.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Contrastive residual-channel monitors with benign-trigger subtraction
- Success threshold: Mean AUROC >= 0.80 for harmful+trigger versus benign+trigger and FPR at 95% TPR <= 0.25 versus clean, without worse-than-baseline clean-policy accuracy.
- Stop condition: Stop if contrastive residual scoring remains below AUROC 0.65 against benign+trigger controls across five seeds or is no better than a token-identity baseline.

## Evidence references

- Artifact root: `<local-path>/projects/agent-safety-via-residual-channel-monitored-activation-anomalies-f053d03063e8`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.

# Asymmetric Anchor-State KV Quantization

Status: `useful_signal`
Curation bucket: `weak_local_only_preserved`
Curation score: `68`
Project ID: `asymmetric-anchor-state-kv-quantization-6c523e897197`
Run ID: `asymmetric-anchor-state-kv-quantization-6c523e897197-20260525T085301544957+0000`

> This is a promising-signal record, not a paper. It is bounded local evidence preserved for possible larger-compute follow-up.

## Deterministic curation

- Bucket: Weak/local-only preserved signals
- Score: `68`
- Score breakdown: `{"bounded_evidence": 20, "evidence_strength": 25, "followup": 0, "hypothesis_status": 15, "source_lineage": 8}`

Reasons:
- moderate evidence_strength
- mixed hypothesis_status
- source lineage present
- local evidence artifact paths are present
- metrics artifact is present
- project decision artifact is present

## Source

- Provider-backed Research Facility batch: hf:zai-org/GLM-5.1: enoch://research-facility/provider/hf:zai-org/GLM-5.1/ebb8877a1709

## What looked useful

Oracle anchors can reduce synthetic output MSE, but practical norm selectors fail; on DistilGPT-2 activations, anchor quantization is 6.05x worse than uniform int4 in output MSE even with oracle anchors and 13.36x to 18.29x worse with norm selectors.

## Boundaries and scale limits

No end-to-end perplexity or generation-quality run, no production KV-cache kernel, no throughput measurement, and no 7B+ or long-context model validation. Synthetic results are mechanistic only; DistilGPT-2 is a small-model proxy.

## Claim scope

Bounded attention-level proxy on synthetic tensors and DistilGPT-2 activations: 2-bit non-anchor plus 8-bit anchor KV quantization does not beat uniform 4-bit KV quantization at the same average bit budget on real activations, even with oracle attention anchors.

## Why it stopped

Early proxy falsification: the most relevant local real-activation test shows worse attention/output fidelity than uniform KV quantization at comparable memory budget.

## Recommended next action

Stop this line as a paper candidate; only revisit with a deployable selector and less destructive non-anchor quantization that first beats uniform 4-bit on a GPT-2-small-class perplexity proxy.

## Follow-up

- Recommended: `false`
- Type: ``
- Title: 
- Success threshold: 
- Stop condition: 

## Evidence references

- Artifact root: `<local-path>/projects/asymmetric-anchor-state-kv-quantization-6c523e897197`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.

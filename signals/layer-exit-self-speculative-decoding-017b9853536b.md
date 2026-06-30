# Layer-Exit Self-Speculative Decoding

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `layer-exit-self-speculative-decoding-017b9853536b`
Run ID: `layer-exit-self-speculative-decoding-017b9853536b-20260523T202642984755+0000`

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

- Provider-backed Research Facility batch: hf:zai-org/GLM-5.1: enoch://research-facility/provider/hf:zai-org/GLM-5.1/71f733db03f9

## What looked useful

Exit 11/12 reached 70.98% top-1 agreement and 2.51 tokens per block-4 verifier cycle, but its draft cost left the best estimated speedup at only 0.8766x baseline. Earlier exits were much cheaper but too inaccurate: exit 9 reached 51.30%, exit 6 22.38%, and exit 3 12.38% agreement.

## Boundaries and scale limits

Tested one GPT-2-small-class model, 40 fixed prompts, 2891 next-token positions, greedy agreement only, and a cost-model speed estimate rather than an optimized production decoder. Does not evaluate trained LayerSkip-style exits or larger models.

## Claim scope

On pretrained GPT-2 small with no early-exit training, intermediate-layer logits can agree with the final layer only when the exit is very deep; the best tested layer-exit self-speculative configuration is estimated slower than full-depth greedy decoding.

## Why it stopped

Proxy/early falsification rather than full validation: direct agreement and acceptance metrics on pretrained GPT-2 show the only accurate exit is too deep to save compute, while practical end-to-end speed would require trained early exits and a real decoder benchmark.

## Recommended next action

Stop this untrained GPT-2 probe; the concrete next bounded test is to train or load explicit early-exit heads and require a layer-6-or-earlier exit to exceed 70% top-1 agreement and 1.1x measured decoding speedup.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Train GPT-2 early exits for self-speculative decoding
- Success threshold: Layer 6 or earlier reaches at least 70% top-1 agreement and an implemented decoder achieves at least 1.1x wall-clock speedup with matched final-model greedy outputs.
- Stop condition: Stop if layer 6 or earlier remains below 60% top-1 agreement after bounded training, or if the implemented decoder remains below 1.0x speedup despite matched outputs.

## Evidence references

- Artifact root: `<local-path>/projects/layer-exit-self-speculative-decoding-017b9853536b`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.

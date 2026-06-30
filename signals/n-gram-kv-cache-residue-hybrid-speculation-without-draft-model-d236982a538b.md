# N-gram + KV-Cache Residue Hybrid Speculation without Draft Model

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `n-gram-kv-cache-residue-hybrid-speculation-without-draft-model-d236982a538b`
Run ID: `n-gram-kv-cache-residue-hybrid-speculation-without-draft-model-d236982a538b-20260524T173337215430+0000`

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

- Provider-backed Research Facility batch: hf:zai-org/GLM-5.1: enoch://research-facility/provider/hf:zai-org/GLM-5.1/1d27f25872ce

## What looked useful

The simple residue hybrid is not robust: 3-gram hybrid accepted 0.3164 tokens per position versus 0.3359 for frequency-only, while 2-gram hybrid accepted 0.2734 versus 0.2383. Residue may help when short n-gram contexts are ambiguous, but it can hurt when frequency statistics are already more specific.

## Boundaries and scale limits

20k GPT-2 tokens, 256 validation and 256 test positions per run, distilgpt2 target only, hidden-state suffix fingerprint proxy rather than direct per-layer KV tensors, no integrated serving latency measurement.

## Claim scope

On Tiny Shakespeare with distilgpt2, a hidden-state residue proxy did not robustly improve draft-model-free n-gram speculative proposals: it underperformed frequency-only for 3-gram contexts but improved target-greedy acceptance for a 2-gram ablation.

## Why it stopped

Proxy/early mixed result rather than full validation: the main 3-gram target metric falsified the simple hybrid, while the 2-gram ablation showed a bounded mechanism signal worth one direct-KV follow-up.

## Recommended next action

Stop this run as no-paper useful signal; run one bounded follow-up that replaces the hidden-state proxy with actual per-layer KV tensor features and requires improvement over frequency-only for both 2-gram and 3-gram contexts.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Direct KV-Tensor Residue Gate for N-gram Speculation
- Success threshold: Direct KV hybrid improves accepted tokens per position by at least 10% over frequency-only for both 2-gram and 3-gram contexts without reducing next-token target-greedy acceptance and with measured scoring overhead below the saved target forward-pass cost.
- Stop condition: Stop as negative if direct KV features fail to beat frequency-only on either 2-gram or 3-gram held-out acceptance, or if scoring overhead exceeds the projected benefit from accepted speculative tokens.

## Evidence references

- Artifact root: `<local-path>/projects/n-gram-kv-cache-residue-hybrid-speculation-without-draft-model-d236982a538b`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.

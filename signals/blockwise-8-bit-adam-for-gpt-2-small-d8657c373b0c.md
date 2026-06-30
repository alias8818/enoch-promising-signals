# Blockwise 8-bit Adam for GPT-2-small

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `blockwise-8-bit-adam-for-gpt-2-small-d8657c373b0c`
Run ID: `blockwise-8-bit-adam-for-gpt-2-small-d8657c373b0c-20260608T095145896320+0000`

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

- Provider-backed Research Facility batch: moonshotai/kimi-k2.6: enoch://research-facility/provider/moonshotai/kimi-k2.6/b2be2b147e7d

## What looked useful

Blockwise 8-bit AdamW can cut persistent optimizer state from about 8.0 to 2.125 bytes/parameter and lower CUDA peak allocation on a GPT-2-small-shaped proxy, but naive per-step dequantize/requantize showed transient loss spikes at lr 1e-4 and divergence/degradation at lr 3e-4 unless block size and learning rate were reduced.

## Boundaries and scale limits

No natural-language corpus, no long training, no perplexity validation, no fused production kernel, no established 8-bit optimizer baseline, and only two GPT-2-small-shaped seeds over 30 synthetic steps.

## Claim scope

Short synthetic GPT-style language-model probes, including an 86.7M-parameter GPT-2-small-shaped model, show that a simple blockwise 8-bit AdamW state representation reduces persistent optimizer-state memory by about 73.4% versus AdamW but introduces stability spikes and is not paper-ready.

## Why it stopped

Proxy evidence supports the memory mechanism but reveals stability spikes and lacks direct natural-language or long-run validation, so this is not a full validation or paper-positive result.

## Recommended next action

Stop this run as no-paper useful signal; next, test a bounded second-moment quantization/scaling variant that must remove transient GPT-2-shaped loss spikes while preserving at least 70% persistent optimizer-state reduction.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Stabilize second-moment quantization for blockwise 8-bit AdamW
- Success threshold: Across at least three seeds, no transient loss spike above 2x AdamW max loss, mean final loss gap below 0.05, and at least 70% persistent optimizer-state memory reduction.
- Stop condition: Stop as negative if the modified quantization still produces loss spikes above 2x AdamW max loss or requires reducing learning rate below the AdamW control to remain stable.

## Evidence references

- Artifact root: `<local-path>/projects/blockwise-8-bit-adam-for-gpt-2-small-d8657c373b0c`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.

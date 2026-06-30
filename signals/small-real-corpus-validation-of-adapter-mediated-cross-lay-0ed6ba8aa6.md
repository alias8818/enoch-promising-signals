# Small Real-Corpus Validation of Adapter-Mediated Cross-Layer KV Sharing

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `small-real-corpus-validation-of-adapter-mediated-cross-lay-0ed6ba8aa6`
Run ID: `small-real-corpus-validation-of-adapter-mediated-cross-lay-0ed6ba8aa6-20260604T073834065397+0000`

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

- Parent run decision: Cross-Layer KV Cache Sharing with Adapters: enoch://control-plane/projects/cross-layer-kv-cache-sharing-with-adapters-02f02cc35faf/runs/cross-layer-kv-cache-sharing-with-adapters-02f02cc35faf-20260604T054604596471+0000
- Provider-backed Research Facility batch: moonshotai/kimi-k2.6: enoch://research-facility/provider/moonshotai/kimi-k2.6/ae31537fae7b

## What looked useful

Cross-layer adapter-mediated K/V sharing is viable enough to train on real text and preserve approximate quality at toy scale, but the tested implementation is consistently worse than a dense baseline and does not improve wall time or memory.

## Boundaries and scale limits

This is a small direct real-corpus training test only. It does not test GPT-2-small scale, modern tokenization, long-context inference KV-cache savings, optimized attention kernels, long training, or downstream robustness.

## Claim scope

On a tiny 4-layer character-level causal language model trained for 1200 steps on Tiny Shakespeare, adapter-mediated previous-layer K/V reuse trains stably and reduces K/V-specific parameters by 65.6%, but trails the dense per-layer K/V baseline by 4.5% mean validation loss across three seeds.

## Why it stopped

Small direct real-corpus evidence produced a useful mechanism signal but not a paper-positive result: shared-adapter KV reuse was stable and parameter-efficient, yet worse than baseline on every seed and slightly slower in the tested implementation.

## Recommended next action

Run a bounded deepen test with a parameter-matched dense baseline and longer training to determine whether the observed 4.5% validation-loss gap is caused by K/V sharing itself or by reduced parameter count/training horizon.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Parameter-Matched Longer Training Test for Adapter-Mediated Cross-Layer KV Sharing
- Success threshold: Shared-adapter mean validation loss no worse than 3% above both dense controls while retaining at least 50% K/V-specific parameter reduction.
- Stop condition: Stop if shared-adapter remains more than 5% worse than either dense control after the longer horizon or shows no closing trend in validation loss.

## Evidence references

- Artifact root: `<local-path>/projects/small-real-corpus-validation-of-adapter-mediated-cross-lay-0ed6ba8aa6`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.

# Pretrained Small-LM Cross-Architecture KV Transfer on Real Text

Status: `useful_signal`
Curation bucket: `likely_stale_low_value_archive`
Curation score: `38`
Project ID: `pretrained-small-lm-cross-architecture-kv-transfer-on-real-baa1b1ac4d`
Run ID: `pretrained-small-lm-cross-architecture-kv-transfer-on-real-baa1b1ac4d-20260614T084058475231+0000`

> This is a promising-signal record, not a paper. It is bounded local evidence preserved for possible larger-compute follow-up.

## Deterministic curation

- Bucket: Likely stale/low-value archive
- Score: `38`
- Score breakdown: `{"bounded_evidence": 20, "evidence_strength": 25, "followup": 0, "hypothesis_status": -15, "source_lineage": 8}`

Reasons:
- moderate evidence_strength
- unsupported hypothesis_status
- source lineage present
- local evidence artifact paths are present
- metrics artifact is present
- project decision artifact is present

## Source

- Parent run decision: Cross-Architecture Prefix KV Transfer in Cascade: enoch://control-plane/projects/cross-architecture-prefix-kv-transfer-in-cascade-b082e90e2b11/runs/cross-architecture-prefix-kv-transfer-in-cascade-b082e90e2b11-20260614T075831613833+0000
- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/7e6034c628f0

## What looked useful

In both directions, target self-cache improved continuation NLL on 32/32 samples, while same-text cross-architecture source cache improved on 0/32 samples and behaved like shuffled source cache. GPT-Neo->GPT-2 cross-cache mean NLL was 9.7013 versus no-prior-context 5.0488 and self-cache 3.6686. GPT-2->GPT-Neo cross-cache mean NLL was 16.8933 versus no-prior-context 5.1633 and self-cache 3.6983.

## Boundaries and scale limits

Tested two small pretrained causal LMs, 32 WikiText-2 validation windows per direction, prompt length 64 and continuation length 16. No learned projection, fine-tuning, larger models, broader datasets, or long-context robustness were tested.

## Claim scope

Raw prompt KV caches are not useful when transferred between pretrained GPT-2 and GPT-Neo-125M on WikiText-2 continuation scoring, despite matching tokenizer, layer count, head count, and head dimension.

## Why it stopped

Controlled small direct real-text test falsified the success threshold: raw same-text cross-cache never improved over no-prior-context in either direction and did not beat shuffled cache reliably.

## Recommended next action

Stop the raw cross-architecture KV transfer claim at this tier; only revisit with an explicit learned alignment/projection mechanism and the same no-context, self-cache, and shuffled-cache controls.

## Follow-up

- Recommended: `false`
- Type: ``
- Title: 
- Success threshold: 
- Stop condition: 

## Evidence references

- Artifact root: `<local-path>/projects/pretrained-small-lm-cross-architecture-kv-transfer-on-real-baa1b1ac4d`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.

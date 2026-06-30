# KV cache 2-bit with attention-impact residual tokens (top 5%)

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `kv-cache-2-bit-with-attention-impact-residual-tokens-top-5-a7546761a851`
Run ID: `kv-cache-2-bit-with-attention-impact-residual-tokens-top-5-a7546761a851-20260613T075535314197+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/9001c3f006c4

## What looked useful

Attention-impact residual tokens provide a modest mechanism signal over all-2bit quantization (7.35% mean KL reduction), but the specific top-5% attention-impact idea is not superior to cheap controls: recency is slightly better by KL and better by top-1/NLL, while random is comparable across five seeds.

## Boundaries and scale limits

Tested only distilgpt2, 12 prompts, 48 next-token positions, 2-bit symmetric per-vector quantization, and oracle next-token attention selection. Not an end-to-end generation, long-context serving, GPT-2-small-or-larger, 7B+, throughput, or non-oracle policy validation.

## Claim scope

On a bounded distilgpt2 next-token KV-cache probe, oracle top-5% attention-impact residual tokens reduce KL versus quantizing all KV vectors to 2-bit, but do not beat simple recency or random 5% residual controls.

## Why it stopped

Early bounded falsification of the specific top-5% attention-impact residual-token claim: the oracle impact selector improved over all-2bit but failed to outperform simpler residual baselines, so this is not paper-ready.

## Recommended next action

Stop as no-paper bounded evidence; only pursue a deepen follow-up if it directly tests GPT-2-small-class or longer-context decode with recency/random controls and a non-oracle impact predictor.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Non-oracle attention-impact residual KV cache on GPT-2-small-class long-context decode
- Success threshold: Attention-impact policy beats recency and random 5% residual controls by at least 10% mean KL or perplexity degradation reduction without worse top-1/NLL behavior, across at least three seeds or prompt shards.
- Stop condition: Stop if the non-oracle policy fails to beat recency by the primary metric or if the oracle upper bound remains within 2% of recency on GPT-2-small-class long-context prompts.

## Evidence references

- Artifact root: `<local-path>/projects/kv-cache-2-bit-with-attention-impact-residual-tokens-top-5-a7546761a851`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.

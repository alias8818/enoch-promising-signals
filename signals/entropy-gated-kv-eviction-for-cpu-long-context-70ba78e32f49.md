# Entropy-Gated KV Eviction for CPU Long Context

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `entropy-gated-kv-eviction-for-cpu-long-context-70ba78e32f49`
Run ID: `entropy-gated-kv-eviction-for-cpu-long-context-70ba78e32f49-20260524T015313102764+0000`

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

- Provider-backed Research Facility batch: hf:moonshotai/Kimi-K2.6: enoch://research-facility/provider/hf:moonshotai/Kimi-K2.6/4d24ceda12ad

## What looked useful

Entropy-gated eviction beat pure recency on average (+0.1407 retained-attention mass) and won 9/20 scenario-budget cases, but it underperformed the best non-gated baseline on average (-0.0368) and failed badly when high-entropy attention was distributed over old context (worst delta -0.2899 versus heavy-hitter).

## Boundaries and scale limits

No real LLM, perplexity, downstream task quality, CPU serving latency, or hardware KV-memory pressure was measured. The full 40-seed length-1024 sweep was stopped for CPU-only efficiency and replaced by a reduced completed sweep.

## Claim scope

Dependency-free synthetic attention-trace simulation of online KV eviction policies at sequence length 512, cache budgets 32/64/128/256, five trace families, and eight seeds.

## Why it stopped

Synthetic proxy evidence is mixed and rejects a general entropy-only superiority claim; it is not full validation of CPU long-context LLM inference.

## Recommended next action

Stop this run as a no-paper useful signal; the next bounded test should replay entropy-gated eviction with an old-context mass or segment-coverage guard on real small-transformer attention traces.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Entropy Gate with Old-Context Coverage Guard on Real Small-Model Attention Traces
- Success threshold: Entropy plus coverage guard beats the best baseline by at least 0.02 mean retained-attention mass or achieves equal retained mass with lower CPU overhead, with no more than 1% relative degradation on task/perplexity proxy.
- Stop condition: Stop if the guarded entropy policy still loses to heavy-hitter/static mixing on diffuse-old or real summarization traces at two or more cache budgets.

## Evidence references

- Artifact root: `<local-path>/projects/entropy-gated-kv-eviction-for-cpu-long-context-70ba78e32f49`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.

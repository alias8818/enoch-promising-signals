# Entropy-Gated KV Eviction for Long Context

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `entropy-gated-kv-eviction-for-long-context-6e3e78913179`
Run ID: `entropy-gated-kv-eviction-for-long-context-6e3e78913179-20260527T200943271689+0000`

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

- Provider-backed Research Facility batch: hf:moonshotai/Kimi-K2.6: enoch://research-facility/provider/hf:moonshotai/Kimi-K2.6/80d69c8860f5

## What looked useful

Entropy contains a small policy-selection signal for mean retained attention mass, but high entropy is not reliably safe to evict under fixed budgets; oracle top-k loss increases with entropy and practical entropy-gating worsens tail loss versus heavy-hitter.

## Boundaries and scale limits

This is an attention-mass proxy, not a real KV-cache serving implementation. It uses GPT-2 only, 768-token contexts, synthetic text, full traced attention entropy, and no next-token loss, retrieval accuracy, latency, or larger-model validation.

## Claim scope

On GPT-2 attention traces at 768 tokens over five varied synthetic long-context examples, an entropy-threshold switch between online heavy-hitter and recency retention improves mean retained attention mass by about 1 to 2 percentage points over heavy-hitter, but does not improve tail loss or safe-loss rate.

## Why it stopped

Proxy attention-trace evidence is mixed: entropy-gating gives small mean kept-mass gains but fails the stronger safety/tail-loss premise and lacks direct generation-quality validation.

## Recommended next action

Stop this run as no-paper useful signal; next run should implement real GPT-2 KV eviction and measure next-token loss or retrieval accuracy before considering scale-up.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Direct GPT-2 KV eviction loss test for entropy-gated retention
- Success threshold: At budgets 64, 128, and 256, entropy-gated eviction improves mean next-token loss or delayed-recall accuracy over online heavy-hitter by at least 2% relative and does not worsen the 95th-percentile per-example loss.
- Stop condition: Stop if entropy-gated eviction fails to beat heavy-hitter on mean quality at two or more budgets, or if it worsens 95th-percentile loss at any budget by more than 1%.

## Evidence references

- Artifact root: `<local-path>/projects/entropy-gated-kv-eviction-for-long-context-6e3e78913179`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.

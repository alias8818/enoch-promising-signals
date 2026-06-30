# Multi-budget generation-time H2O KV-cache curves on perplexity and passkey retrieval

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `multi-budget-generation-time-h2o-kv-cache-curves-on-perple-9034402ea1`
Run ID: `multi-budget-generation-time-h2o-kv-cache-curves-on-perple-9034402ea1-20260529T214713298560+0000`

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

- Parent run decision: H2O heavy-hitter KV eviction for long local context: enoch://control-plane/projects/h2o-heavy-hitter-kv-eviction-for-long-local-context-c669d3a1deb4/runs/h2o-heavy-hitter-kv-eviction-for-long-local-context-c669d3a1deb4-20260529T064021255382+0000
- Parent run decision: Generation-time H2O KV-cache perplexity and retrieval test: enoch://control-plane/projects/generation-time-h2o-kv-cache-perplexity-and-retrieval-test-7c92ff1c63/runs/generation-time-h2o-kv-cache-perplexity-and-retrieval-test-7c92ff1c63-20260529T163033316561+0000

## What looked useful

H2O gave much lower Wikitext-2 PPL than recent-only/random at 64-128 token cache budgets and lower passkey answer NLL than controls at 64-128, but passkey exact-match was 0 for all policies including full-cache and target rank was noisy.

## Boundaries and scale limits

Single small GPT-2-class model, 512-token natural-text windows, synthetic passkey prompts, no batching or serving latency, no larger/copy-capable model family, and 512-token budget is effectively full-cache for the PPL setting.

## Claim scope

On distilgpt2 with 3 fixed seeds, 12 Wikitext-2 512-token windows per seed, and synthetic 384-token-prefix passkey prompts, generation-time H2O KV eviction outperforms recent-only and random controls on perplexity at tight budgets and improves passkey answer NLL at 64-128 token budgets, but it does not show exact passkey retrieval.

## Why it stopped

Tier 2 evidence supports a bounded mechanism/practical signal for perplexity and answer NLL, but the direct passkey retrieval metric failed even for full-cache and the evidence is not publication-grade.

## Recommended next action

Stop paper path for this run; run one bounded deepen follow-up on a copy-capable small model and longer prompts where full-cache passkey exact-match is high before making any retrieval claim.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Copy-capable long-prefix H2O passkey exact-match curves
- Success threshold: H2O retains at least 70% exact-match at one compressed budget where recent-only and random are each at least 20 percentage points worse, while PPL degradation remains below the recent-only control.
- Stop condition: Stop if no locally runnable model/prompt combination reaches 80% full-cache passkey exact-match, or if H2O fails to beat both recent-only and random on exact-match at all compressed budgets.

## Evidence references

- Artifact root: `<local-path>/projects/multi-budget-generation-time-h2o-kv-cache-curves-on-perple-9034402ea1`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.

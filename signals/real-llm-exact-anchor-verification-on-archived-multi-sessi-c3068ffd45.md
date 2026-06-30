# Real-LLM exact-anchor verification on archived multi-session agent traces

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `real-llm-exact-anchor-verification-on-archived-multi-sessi-c3068ffd45`
Run ID: `real-llm-exact-anchor-verification-on-archived-multi-sessi-c3068ffd45-20260613T191104442554+0000`

> This is a promising-signal record, not a paper. It is bounded local evidence preserved for possible larger-compute follow-up.

## Deterministic curation

- Bucket: Top external-researcher candidates
- Score: `98`
- Score breakdown: `{"bounded_evidence": 20, "evidence_strength": 25, "followup": 15, "hypothesis_status": 30, "source_lineage": 8}`

Reasons:
- moderate evidence_strength
- supported hypothesis_status
- source lineage present
- bounded follow-up is specified
- local evidence artifact paths are present
- metrics artifact is present
- project decision artifact is present

## Source

- Parent run decision: Exact-Anchor Compressed Memory for Multi-Session Agent Runs: enoch://control-plane/projects/exact-anchor-compressed-memory-for-multi-session-agent-runs-e2c85b033684/runs/exact-anchor-compressed-memory-for-multi-session-agent-runs-e2c85b033684-20260613T182327483522+0000
- Parent run decision: LLM-in-the-loop exact-anchor memory on realistic multi-session agent traces: enoch://control-plane/projects/llm-in-the-loop-exact-anchor-memory-on-realistic-multi-ses-fced480199/runs/llm-in-the-loop-exact-anchor-memory-on-realistic-multi-ses-fced480199-20260613T185004768881+0000

## What looked useful

Exact-anchor prompting was instruction-sensitive and effective on this bounded archive: exact prompt 108/108 accuracy with 0 false positives; loose prompt 103/108 with 5 false positives; token-overlap baseline 84/108 with 24 false positives.

## Boundaries and scale limits

Single configured Codex model path, one local archived trace corpus, 108 cases, clipped 1450-character contexts, deterministic construction of positives and negatives, no independent model-family replication, no adversarially selected anchors, no long-document citation workflow, and no external corpus.

## Claim scope

On a fixed-seed benchmark of 108 exact-anchor cases constructed from 36 archived Enoch/Codex multi-session trace excerpts, a configured Codex real-LLM judge with strict exact-substring instructions matched the deterministic exact oracle and outperformed a token-overlap baseline and a loose-prompt ablation on near-match negative controls.

## Why it stopped

Tier-2 local confirmation produced useful mechanism evidence but remains too narrow and local for publication readiness.

## Recommended next action

Run a bounded deepen follow-up with at least two independent model families and adversarial whitespace, punctuation, homoglyph, and repeated-near-duplicate anchors before considering any paper-positive gate.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Cross-model adversarial exact-anchor verification on archived agent traces
- Success threshold: Exact-anchor prompt accuracy at least 98% overall with false-positive rate below 2% in every negative-control condition for each tested model family, and at least 10 percentage-point accuracy improvement over loose semantic prompt or token-overlap baseline on adversarial negatives.
- Stop condition: Stop if any tested model family exceeds 5% false-positive rate on adversarial negative controls under exact instructions or if the exact prompt fails to improve over the stronger non-oracle baseline by at least 5 percentage points.

## Evidence references

- Artifact root: `<local-path>/projects/real-llm-exact-anchor-verification-on-archived-multi-sessi-c3068ffd45`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.

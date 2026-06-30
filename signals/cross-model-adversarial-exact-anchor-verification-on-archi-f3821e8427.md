# Cross-model adversarial exact-anchor verification on archived agent traces

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `93`
Project ID: `cross-model-adversarial-exact-anchor-verification-on-archi-f3821e8427`
Run ID: `cross-model-adversarial-exact-anchor-verification-on-archi-f3821e8427-20260613T194134008255+0000`

> This is a promising-signal record, not a paper. It is bounded local evidence preserved for possible larger-compute follow-up.

## Deterministic curation

- Bucket: Top external-researcher candidates
- Score: `93`
- Score breakdown: `{"bounded_evidence": 20, "evidence_strength": 25, "followup": 10, "hypothesis_status": 30, "source_lineage": 8}`

Reasons:
- moderate evidence_strength
- supported hypothesis_status
- source lineage present
- bounded follow-up is specified
- follow-up depth is already high
- local evidence artifact paths are present
- metrics artifact is present
- project decision artifact is present

## Source

- Parent run decision: Real-LLM exact-anchor verification on archived multi-session agent traces: enoch://control-plane/projects/real-llm-exact-anchor-verification-on-archived-multi-sessi-c3068ffd45/runs/real-llm-exact-anchor-verification-on-archived-multi-sessi-c3068ffd45-20260613T191104442554+0000
- Parent run decision: LLM-in-the-loop exact-anchor memory on realistic multi-session agent traces: enoch://control-plane/projects/llm-in-the-loop-exact-anchor-memory-on-realistic-multi-ses-fced480199/runs/llm-in-the-loop-exact-anchor-memory-on-realistic-multi-ses-fced480199-20260613T185004768881+0000

## What looked useful

Across 28,800 deterministic claims from five fixed seeds, the exact verifier achieved 0.0000 false accept rate and 0.0000 false reject rate. The fuzzy baseline had 0.8684 false accept rate; no-line-check and normalized-exact ablations had 0.1132 and 0.2767 false accept rates respectively.

## Boundaries and scale limits

The corpus is one local archived Codex JSONL trace plus prompt/control files. Cross-model behavior was approximated with deterministic model-style perturbation profiles, not live outputs from independent LLMs. Multi-line anchors, larger trace archives, and real model-generated adversarial claims remain untested.

## Claim scope

On the local archived Codex trace and prompt/control files in this project, a strict verifier requiring matching file, byte span, line number, and exact quoted text rejected all generated invalid adversarial anchor claims while accepting all true exact anchors.

## Why it stopped

No-paper useful signal: the mechanism is supported locally, but the cross-model claim is proxied by deterministic style profiles and the archived corpus is too small for publication-grade validation.

## Recommended next action

Stop paper escalation for this run; deepen only with real multi-model adversarial anchor outputs over a larger held-out archived trace corpus.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Real multi-model exact-anchor adversarial verification on held-out archived traces
- Success threshold: Exact verifier false accept rate <= 0.005 and false reject rate <= 0.01 on at least 5,000 labeled real-model anchor claims, with at least 10x lower false accept rate than the fuzzy baseline.
- Stop condition: Stop if real-model invalid anchors produce exact-verifier false accept rate above 0.02 after duplicate-valid adjudication, or if a held-out trace corpus with stable byte/line anchors cannot be assembled.

## Evidence references

- Artifact root: `<local-path>/projects/cross-model-adversarial-exact-anchor-verification-on-archi-f3821e8427`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
